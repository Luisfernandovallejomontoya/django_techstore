from django.db import models
from django.conf import settings
from productos.models import Producto

class CampanaPublicitaria(models.Model):
    TIPOS_DE_CAMPANA = (
        ('basica', 'Campaña Básica'),
        ('pro', 'Campaña Pro'),
        ('premium', 'Campaña Premium'),
    )

    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS_DE_CAMPANA, default='basica')
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True)
    activa = models.BooleanField(default=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

class Anuncio(models.Model):
    campana = models.ForeignKey(CampanaPublicitaria, on_delete=models.CASCADE, related_name='anuncios')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    clics = models.PositiveIntegerField(default=0)
    impresiones = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Anuncio para {self.producto.nombre}"