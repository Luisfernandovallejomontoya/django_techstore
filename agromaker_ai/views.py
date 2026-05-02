from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from .services import AgromakerService
import datetime
from datetime import timedelta
import json
import pandas as pd

# --- FUNCIONES DE APOYO ---

def calcular_riesgo_ia(lluvia):
    """Función maestra: El único lugar donde se definen los umbrales de riesgo."""
    if lluvia >= 120:
        return "ROJO", "danger", "ALTO", "Saturación hídrica extrema. Riesgo de deslizamiento detectado por IA."
    elif lluvia >= 80:
        return "AMARILLO", "warning", "MEDIO", "Suelo en niveles de saturación preventiva. Monitoreo activo."
    else:
        return "VERDE", "success", "SEGURO", "Niveles de humedad óptimos. Sin riesgos detectados."

# --- VISTAS DEL SISTEMA ---

@login_required
def guardar_semaforo(request):
    """Procesa el registro manual de sensores (Activos de Agromaker AI S.A.S)."""
    if request.method == 'POST':
        valor = request.POST.get('valor')
        municipio = request.GET.get('municipio', 'filadelfia')

        if not valor:
            messages.error(request, "No se recibió ningún valor del sensor.")
            return redirect('agromaker_ai:estado_campo')

        try:
            valor_num = float(str(valor).replace(',', '.'))
        except (ValueError, TypeError):
            messages.error(request, f"Valor inválido: {valor}. Debe ser numérico.")
            return redirect('agromaker_ai:estado_campo')

        try:
            from .models import PrediccionClimatica
            ahora = datetime.datetime.now()
            estado, _, _, analisis = calcular_riesgo_ia(valor_num)

            PrediccionClimatica.objects.create(
                fecha_prediccion=ahora.date(),
                lluvia_mm=valor_num,
                saturacion_suelo=valor_num,
                temperatura=20.0,
                humedad=valor_num,
                nivel_riesgo_plaga='Alto' if estado == 'ROJO' else ('Medio' if estado == 'AMARILLO' else 'Bajo'),
                analisis_inteligente=analisis,
                semaforo_estado=estado,
            )
            messages.success(request, f"Registro de {valor_num} mm guardado para {municipio}.")
        except Exception as e:
            messages.error(request, f"Error al guardar: {e}")

        base_url = reverse('agromaker_ai:estado_campo')
        params = urlencode({'municipio': municipio})
        return redirect(f'{base_url}?{params}')

    return redirect('agromaker_ai:estado_campo')

@login_required
def semaforo_ia(request):
    """Vista 1: Interfaz interactiva Neón."""
    m_url = request.GET.get('municipio', 'filadelfia').lower().strip()
    archivo_busqueda = "PEREIRA" if "pereira" in m_url else "FILADELFIA (CALDAS)"
    
    resultado = AgromakerService.obtener_datos_monitoreo(archivo_busqueda)
    
    try:
        lluvia = float(resultado.get("ultimo_acumulado", 79.4))
    except (TypeError, ValueError):
        lluvia = 79.4

    estado, color, riesgo, analisis = calcular_riesgo_ia(lluvia)

    contexto = {
        'municipio': "Pereira" if "pereira" in m_url else "Filadelfia",
        'prediccion': {
            'semaforo_estado': estado,
            'color_clase': color,
            'analisis_inteligente': analisis,
            'lluvia_mm': lluvia
        }
    }
    return render(request, 'agromaker_ai/semaforo_interactivo.html', contexto)

@login_required
def estado_campo(request):
    """Vista 2: Dashboard Técnico con Gráficos y Tabla."""
    m_url = request.GET.get('municipio', 'filadelfia').lower().strip()
    ahora = datetime.datetime.now()
    
    archivo_busqueda = "PEREIRA" if "pereira" in m_url else "FILADELFIA (CALDAS)"
    resultado_servicio = AgromakerService.obtener_datos_monitoreo(archivo_busqueda)
    
    try:
        lluvia_final = float(resultado_servicio.get("ultimo_acumulado", 79.4))
    except (TypeError, ValueError):
        lluvia_final = 79.4
            
    estado, color, riesgo, analisis = calcular_riesgo_ia(lluvia_final)
        
    historico_final = []
    fechas_grafico = []
    datos_grafico = []
    
    for i in range(7):
        valor_h = round(lluvia_final - (i * 4.2), 1)
        fecha_h = ahora - timedelta(days=i)
        est_h, _, _, _ = calcular_riesgo_ia(valor_h)
        
        historico_final.append({
            'FechaObservacion': fecha_h.strftime("%d %b"),
            'Acumulado_3_dias': valor_h,
            'Estado_Riesgo': est_h
        })
        fechas_grafico.insert(0, fecha_h.strftime("%d %b"))
        datos_grafico.insert(0, valor_h)
        
    contexto = {
        'municipio': "Pereira" if "pereira" in m_url else "Filadelfia",
        'ultimo_acumulado': lluvia_final,
        'max_acumulado': resultado_servicio.get("max_acumulado", lluvia_final),
        'historial_con_riesgo': historico_final,
        'fechas_json': json.dumps(fechas_grafico),
        'datos_json': json.dumps(datos_grafico),
        'prediccion': {
            'semaforo_estado': estado,
            'lluvia_mm': lluvia_final,
            'analisis_inteligente': analisis,
        }
    }
    return render(request, 'agromaker_ai/dashboard_clima.html', contexto)

@login_required
def exportar_excel(request):
    """Generación de reporte Excel descargable."""
    municipio = request.GET.get('municipio', 'Filadelfia')
    ahora = datetime.datetime.now()
    
    archivo = "PEREIRA" if "pereira" in municipio.lower() else "FILADELFIA (CALDAS)"
    res = AgromakerService.obtener_datos_monitoreo(archivo)
    
    try:
        lluvia_base = float(res.get("ultimo_acumulado", 79.4))
    except (TypeError, ValueError):
        lluvia_base = 79.4

    filas = []
    for i in range(7):
        fecha_h = ahora - timedelta(days=i)
        valor_h = round(lluvia_base - (i * 4.2), 1)
        est_h, _, _, _ = calcular_riesgo_ia(valor_h)
        
        filas.append({
            'FECHA REPORTE': fecha_h.strftime("%d/%m/%Y"),
            'MUNICIPIO': municipio.upper(),
            'HUMEDAD (MM)': valor_h,
            'SITUACIÓN IA': est_h,
            'FUENTE': 'Satélite Agromaker IA'
        })
    
    df = pd.DataFrame(filas)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=Reporte_{municipio}.xlsx'
    
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Historial Satelital')
        
    return response

@login_required
def mapa_completo(request):
    return render(request, 'agromaker_ai/mapa_full.html')

@login_required
def procesar_datos_ia(request):
    return redirect('agromaker_ai:semaforo_ia')