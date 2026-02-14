from django.contrib import admin
from .models import PrediccionClimatica

@admin.register(PrediccionClimatica)
class PrediccionClimaticaAdmin(admin.ModelAdmin):
    # Esto es lo que verás en la tabla principal
    list_display = ('fecha_prediccion', 'lluvia_mm', 'nivel_riesgo_plaga', 'semaforo_estado')
    
    # Filtros para que busques por clima o riesgo
    list_filter = ('semaforo_estado', 'nivel_riesgo_plaga')
    
    # Campo de búsqueda para tus notas de la IA
    search_fields = ('analisis_ia',)