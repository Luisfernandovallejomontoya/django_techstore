# 🔓 Archivo: productos/urls.py
# 📌 Define las rutas (URLs) que se conectan a las vistas de la app productos

from django.urls import path
from . import views  # ✅ Importa todas las vistas locales desde productos/views.py

# 🧭 Lista de rutas disponibles en esta app
urlpatterns = [
    # 🌐 Ruta raíz de productos: muestra el catálogo principal
    path('', views.index, name='index'),  # Plantilla: productos/index.html

    # 📦 Catálogo completo desde la base de datos
    path('catalogo/', views.catalogo, name='catalogo'),  # Asegúrate que la vista exista en views.py

    # 🖼️ Galería estática local (no usa base de datos)
    path('galeria/', views.galeria_local, name='galeria_local'),  # Requiere plantilla galeria.html

    # 🛒 Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),  # Muestra todos los productos agregados

    # ➕ Agrega producto al carrito (usando su ID)
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

    # ➖ Quita producto completamente del carrito
    path('carrito/quitar/<int:producto_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),

    # 🔼 Aumenta la cantidad de un producto en el carrito
    path('carrito/aumentar/<int:producto_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),

    # 🔽 Reduce la cantidad de un producto (mínimo 1)
    path('carrito/reducir/<int:producto_id>/', views.reducir_cantidad, name='reducir_cantidad'),
]