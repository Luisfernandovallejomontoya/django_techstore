from django.shortcuts import render, redirect
from .models import RegistroSuelo

def dashboard_suelos(request):
    """ Historial técnico completo para auditoría de activos (Fondo 305 CEO) """
    registros = RegistroSuelo.objects.all().order_by('-fecha')
    return render(request, 'agromaker_soil/dashboard.html', {'registros': registros})

def reporte_campesino(request):
    """ Lógica de IA: Semáforo pedagógico para Filadelfia """
    ultimo_registro = RegistroSuelo.objects.last()
    todos_los_registros = RegistroSuelo.objects.all().order_by('-fecha')
    
    # Valores por defecto para el sistema
    alerta = "ESTADO ÓPTIMO"
    recomendacion = "Puede proceder con las labores programadas."
    color = "verde"

    if ultimo_registro:
        # Sincronización: Extraemos la humedad de la columna 'conductividad'
        val_humedad = getattr(ultimo_registro, 'conductividad', 0)
        
        # Conversión segura (Blindaje contra comas de teclados de tablets)
        try:
            val_humedad_num = float(str(val_humedad).replace(',', '.')) if val_humedad else 0
            val_ph_num = float(str(ultimo_registro.ph).replace(',', '.')) if ultimo_registro.ph else 7.0
        except (ValueError, TypeError):
            val_humedad_num = 0
            val_ph_num = 7.0
        
        # --- MOTOR DE DECISIONES IA AGROMAKER ---
        if val_ph_num < 5.5:
            alerta = "ALERTA DE ACIDEZ"
            recomendacion = "Aplicar enmienda (cal agrícola) para corregir el pH."
            color = "rojo"
        elif val_humedad_num > 80:
            alerta = "SATURACIÓN POR LLUVIA"
            recomendacion = "SUSPENDER FERTILIZACIÓN. Suelo saturado, riesgo de lixiviación."
            color = "naranja"

    contexto = {
        'registro': ultimo_registro,
        'registros': todos_los_registros, 
        'alerta': alerta,
        'recomendacion': recomendacion,
        'color': color,
        'municipio': 'Filadelfia, Caldas'
    }
    return render(request, 'agromaker_soil/dashboard.html', contexto)

def registrar_dato(request):
    """ Inyector de datos: Mapea la entrada 'humedad' a la columna 'conductividad' """
    if request.method == "POST":
        lote_nombre = request.POST.get('lote')
        ph_valor = request.POST.get('ph')
        h_val = request.POST.get('humedad') 

        # LIMPIEZA: Convertimos comas en puntos para no romper la base de datos
        if ph_valor: ph_valor = ph_valor.replace(',', '.')
        if h_val: h_val = h_val.replace(',', '.')

        # GUARDADO CRÍTICO: Usamos 'conductividad' como nombre de columna real
        RegistroSuelo.objects.create(
            lote=lote_nombre,
            ph=ph_valor,
            conductividad=h_val, 
            observaciones=f"Activo Subsidiado - Sincronización Filadelfia"
        )
        return redirect('reporte_campesino') 
    
    return render(request, 'agromaker_soil/registrar.html')