from django.db import models
from .helpers import humedad_coherente

class RegistroSuelo(models.Model):
    # Campos base del sistema
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Muestreo")
    lote = models.CharField(max_length=100, default="Filadelfia - Lote Principal")
    ph = models.FloatField(verbose_name="Nivel de pH (0-14)")
    humedad = models.FloatField(default=0, verbose_name="Humedad (%)")
    conductividad = models.FloatField(null=True, blank=True, verbose_name="Conductividad Eléctrica")
    observaciones = models.TextField(blank=True, verbose_name="Notas de Campo")

    class Meta:
        verbose_name = "Registro de Suelo"
        verbose_name_plural = "Monitoreo de Suelos"

    def __str__(self):
        return f"{self.lote} - pH {self.ph} ({self.fecha.strftime('%d/%m/%Y')})"

    @property
    def humedad_lectura(self) -> float:
        """Porcentaje coherente (resuelve lógica entre conductividad y humedad)."""
        return humedad_coherente(self)

    @property
    def estado_semaforo(self):
        """Importación local para evitar dependencia circular con semaforo.py"""
        from .semaforo import evaluar_estado_suelo
        return evaluar_estado_suelo(self)

    @property
    def interpretacion_ph(self):
        """Etiqueta dinámica para el encabezado del dashboard."""
        return self.estado_semaforo.etiqueta_tarjeta