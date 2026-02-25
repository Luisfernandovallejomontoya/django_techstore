from django.db import models

class RegistroSuelo(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Muestreo")
    lote = models.CharField(max_length=100, default="Filadelfia - Lote Principal")
    ph = models.FloatField(verbose_name="Nivel de pH (0-14)")
    conductividad = models.FloatField(null=True, blank=True, verbose_name="Conductividad Eléctrica")
    observaciones = models.TextField(blank=True, verbose_name="Notas de Campo")

    class Meta:
        verbose_name = "Registro de Suelo"
        verbose_name_plural = "Monitoreo de Suelos"

    def __str__(self):
        return f"{self.lote} - pH {self.ph} ({self.fecha.strftime('%d/%m/%Y')})"

   
   
    @property
    def interpretacion_ph(self):
        """Lógica de IA para clasificar el tipo de suelo según pH"""
        # Agregamos esta validación para evitar el error de 'NoneType'
        if self.ph is None:
            return "Esperando dato..."
            
        if self.ph < 5.5:
            return "🔴 FUERTEMENTE ÁCIDO (Requiere Enmienda)"
        elif 5.5 <= self.ph <= 7.0:
            return "🟢 ÓPTIMO / NEUTRO"
        else:
            return "🔵 ALCALINO"