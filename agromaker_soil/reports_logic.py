# agromaker_soil/reports_logic.py
from .models import RegistroSuelo
from django.utils import timezone
from datetime import timedelta

def analizar_monitoreo_nocturno():
    ahora = timezone.now()
    hace_12_horas = ahora - timedelta(hours=12)
    
    # Filtramos solo los datos capturados en las últimas 12 horas
    registros = RegistroSuelo.objects.filter(fecha__gte=hace_12_horas).order_by('fecha')
    
    if not registros.exists():
        return {
            'total_lecturas': 0,
            'ph_promedio': 0,
            'humedad_maxima': 0,
            'alerta_critica': False
        }

    # PROCESAMIENTO DE DATOS CON LIMPIEZA (Paso Pedagógico)
    # Convertimos a float y reemplazamos comas por puntos para evitar errores de cálculo
    lista_ph = []
    lista_humedad = []
    
    for r in registros:
        try:
            val_ph = float(str(r.ph).replace(',', '.')) if r.ph else 7.0
            # CORRECCIÓN VITAL: Usamos 'conductividad' que es donde guardamos la humedad
            val_h = float(str(r.conductividad).replace(',', '.')) if r.conductividad else 0.0
            lista_ph.append(val_ph)
            lista_humedad.append(val_h)
        except (ValueError, TypeError):
            continue

    reporte = {
        'total_lecturas': registros.count(),
        'ph_promedio': sum(lista_ph) / len(lista_ph) if lista_ph else 0,
        'humedad_maxima': max(lista_humedad) if lista_humedad else 0,
        'alerta_critica': False
    }
    
    # Lógica de IA: Si la humedad superó el 88%, marcar alerta para el CEO
    if reporte['humedad_maxima'] >= 88.0:
        reporte['alerta_critica'] = True
        
    return reporte