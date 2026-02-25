from django.contrib import admin
from .models import RegistroSuelo

@admin.register(RegistroSuelo)
class RegistroSueloAdmin(admin.ModelAdmin):
    # Mira el espacio a la izquierda de estas líneas (es vital)
    list_display = ('lote', 'ph', 'interpretacion_ph', 'fecha')
    list_filter = ('lote', 'fecha')
    readonly_fields = ('interpretacion_ph',)
    ordering = ('-fecha',)