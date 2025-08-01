# 📌 Define los modelos de Producto, Pedido y DetallePedido

from django.db import models
# from usuarios.models import Usuario
from django.utils.translation import gettext_lazy as _

# 📦 Modelo de producto disponible en la tienda
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

# 🧾 Pedido realizado por un usuario
class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'Pendiente', _('Pendiente')
        PAGADO = 'Pagado', _('Pagado')
        ENVIADO = 'Enviado', _('Enviado')
        ENTREGADO = 'Entregado', _('Entregado')

    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha_pedido']

    def calcular_total(self):
        return sum(detalle.subtotal() for detalle in self.detallepedido_set.all())

    def __str__(self):
        return f"Pedido #{self.id} - - {self.estado}"

# 📋 Detalles de los productos dentro de cada pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedidos'

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def save(self, *args, **kwargs):
        # ⚙️ Autoasignar precio al crear el detalle
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido #{self.pedido.id})"