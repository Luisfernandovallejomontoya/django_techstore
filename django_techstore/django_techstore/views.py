from django.shortcuts import render
from django.http import HttpResponse
from .services import AgromakerService 
from .models import PrediccionClimatica 

# PEDAGOGÍA: Centralizamos el nombre del archivo para fácil mantenimiento
ARCHIVO_FUENTE = "clima_filadelfia.csv"

def procesar_datos_ia(request):
    """
    Analiza el historial masivo desde CSV y lo muestra en el Dashboard.
    """
    resultado = AgromakerService.cargar_datos_csv(ARCHIVO_FUENTE)
    
    if "error" in resultado:
        return render(request, 'agromaker_ai/dashboard.html', {"error": resultado["error"]})
    
    # Agregamos el título al diccionario de resultados
    resultado['titulo'] = "Dashboard de Inteligencia Climática"
    
    # Servimos los datos en la plantilla visual
    return render(request, 'agromaker_ai/dashboard.html', resultado)

def estado_campo(request):
    """
    Monitor en tiempo real: Muestra el semáforo del último registro del Admin.
    """
    try:
        # Buscamos el registro más reciente de forma eficiente
        ultima_prediccion = PrediccionClimatica.objects.latest('fecha_registro')
        hay_datos = True
    except PrediccionClimatica.DoesNotExist:
        ultima_prediccion = None
        hay_datos = False

    contexto = {
        'prediccion': ultima_prediccion,
        'hay_datos': hay_datos,
        'titulo': "Monitor en Vivo - Filadelfia"
    }
    return render(request, 'agromaker_ai/estado_actual.html', contexto)

def exportar_riesgo_excel(request):
    """Genera el reporte Excel basado en el CSV."""
    resultado = AgromakerService.cargar_datos_csv(ARCHIVO_FUENTE)
    if "error" in resultado:
        return HttpResponse("Error al generar reporte", status=404)

    contenido_excel = AgromakerService.generar_excel(resultado.get("historial_con_riesgo", []))
    response = HttpResponse(
        contenido_excel, 
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=Reporte_Agromaker_Filadelfia.xlsx'
    return response