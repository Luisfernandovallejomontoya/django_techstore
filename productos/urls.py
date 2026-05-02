from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('restar/<int:producto_id>/', views.restar_del_carrito, name='restar_del_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('procesar_pedido/', views.procesar_pedido, name='procesar_pedido'),
    path('galeria/', views.galeria_local, name='galeria_local'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]