# 📌 Define los modelos de Producto, Pedido y DetallePedido

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import os  # ¡IMPORTANTE: Asegúrate de importar el módulo 'os' aquí!

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
    # ¡CRÍTICO! upload_to='' para que las imágenes estén directamente en la carpeta media.
    # Esto ya lo tenías bien.
    imagen = models.ImageField(upload_to='', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    # --- INICIO DE LA CORRECCIÓN PARA GESTIÓN DE IMÁGENES ---
    # Sobreescribe el método save() para manejar la eliminación de imágenes antiguas.
    def save(self, *args, **kwargs):
        # Si el objeto ya existe en la base de datos (es decir, estamos editando un producto existente)
        if self.pk:
            try:
                # Obtenemos la versión antigua del producto de la base de datos
                old_instance = Producto.objects.get(pk=self.pk)
                # Verificamos si la imagen ha cambiado
                # Si había una imagen antigua Y la nueva imagen es diferente
                if old_instance.imagen and old_instance.imagen != self.imagen:
                    # Construimos la ruta completa al archivo de la imagen antigua
                    old_image_path = old_instance.imagen.path
                    # Verificamos si el archivo existe físicamente en el disco
                    if os.path.exists(old_image_path):
                        # Si existe, lo borramos para evitar duplicados
                        os.remove(old_image_path)
            except Producto.DoesNotExist:
                # Esto ocurre si es un objeto nuevo o no se encontró la instancia antigua.
                # No hay imagen antigua que borrar en este caso.
                pass
        
        # Llama al método save() original de la clase padre (models.Model)
        # Esto guarda el nuevo producto o actualiza el existente y su nueva imagen.
        super().save(*args, **kwargs)

    # Opcional pero recomendado: Sobreescribe el método delete()
    # para borrar la imagen del disco cuando un producto es eliminado desde el admin.
    def delete(self, *args, **kwargs):
        if self.imagen:
            # Construimos la ruta completa al archivo de la imagen
            image_path = self.imagen.path
            # Verificamos si el archivo existe físicamente en el disco
            if os.path.exists(image_path):
                # Si existe, lo borramos
                os.remove(image_path)
        # Llama al método delete() original de la clase padre
        super().delete(*args, **kwargs)
    # --- FIN DE LA CORRECCIÓN PARA GESTIÓN DE IMÁGENES ---


# 🧾 Pedido realizado por un usuario
class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'Pendiente', _('Pendiente')
        PAGADO = 'Pagado', _('Pagado')
        ENVIADO = 'Enviado', _('Enviado')
        ENTREGADO = 'Entregado', _('Entregado')

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha_pedido']

    def calcular_total(self):
        return sum(detalle.subtotal() for detalle in self.detalles.all())

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username} - {self.estado}"

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
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido #{self.pedido.id})"