from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from django.contrib.auth import get_user_model

# Obtiene el modelo de usuario activo en el proyecto
User = get_user_model()


# 🏷️ Modelo para las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# 📦 Modelo de producto disponible en la tienda
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    # Maneja la eliminación de imágenes antiguas al actualizar
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Producto.objects.get(pk=self.pk)
                if old_instance.imagen and old_instance.imagen != self.imagen:
                    old_image_path = old_instance.imagen.path
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
            except Producto.DoesNotExist:
                pass
        
        super().save(*args, **kwargs)

    # Maneja la eliminación de la imagen al borrar el producto
    def delete(self, *args, **kwargs):
        if self.imagen:
            image_path = self.imagen.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)


# 🛒 Modelo para la orden de compra
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_productos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=50, default='Pendiente')
    
    def __str__(self):
        return f"Pedido de {self.user.username} - {self.fecha_creacion}"


# 🛍️ Modelo para los productos dentro de la orden
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='detalles_pedido_productos')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"