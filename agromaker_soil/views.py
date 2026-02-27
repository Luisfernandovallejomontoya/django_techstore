from django.shortcuts import render
from .models import RegistroSuelo

def dashboard_suelos(request):
    # Traemos todos los registros, del más nuevo al más viejo
    registros = RegistroSuelo.objects.all().order_by('-fecha')
    
    # Enviamos los datos a una plantilla HTML que crearemos después
    return render(request, 'agromaker_soil/dashboard.html', {'registros': registros})

def reporte_campesino(request):
    ultimo_registro = RegistroSuelo.objects.last()
    
    alerta = "ESTADO ÓPTIMO"
    recomendacion = "Puede proceder con las labores programadas."
    color = "verde"

    # Verificamos si el registro existe para evitar errores
    if ultimo_registro:
        # Aquí es donde estaba el error. 
        # Si tu modelo tiene 'ph', verifica si el otro es 'humedad' o 'nivel_humedad'
        try:
            val_humedad = ultimo_registro.humedad 
        except AttributeError:
            # Si falla, es porque en el modelo se llama diferente (ej: nivel_humedad)
            val_humedad = getattr(ultimo_registro, 'nivel_humedad', 0)

        if ultimo_registro.ph < 5.5:
            alerta = "ALERTA DE ACIDEZ"
            recomendacion = "Aplicar enmienda (cal agrícola)."
            color = "rojo"
        elif val_humedad > 80:
            alerta = "SATURACIÓN POR LLUVIA"
            recomendacion = "SUSPENDER FERTILIZACIÓN inmediata."
            color = "naranja"

    contexto = {
        'registro': ultimo_registro,
        'alerta': alerta,
        'recomendacion': recomendacion,
        'color': color,
        'municipio': 'Filadelfia, Caldas'
    }
    
    return render(request, 'agromaker_soil/dashboard.html', contexto)


