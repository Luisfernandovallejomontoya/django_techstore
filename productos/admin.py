from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido

# Registra tus modelos en el panel de administración
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)