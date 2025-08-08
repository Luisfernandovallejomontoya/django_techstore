from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    # Otros campos que necesites, como 'direccion', 'metodo_pago', etc.

    def __str__(self):
        return f'Pedido #{self.id}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
