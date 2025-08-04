from django.contrib import admin

# Register your models here.
# productos/admin.py

from .models import Categoria, Producto, Pedido, DetallePedido # Importa todos tus modelos

# Registra cada modelo para que aparezca en el panel de administración
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)