# productos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mantenemos las vistas index y catalogo separadas
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    
    # URLs para el carrito
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('restar/<int:producto_id>/', views.restar_del_carrito, name='restar_del_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),

    # Otras URLs
    path('galeria/', views.galeria_local, name='galeria_local'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]