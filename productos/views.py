# productos/views.py

import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from productos.models import Producto
from .carrito import Carrito
from django.urls import reverse

# Vista de detalle
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    context = {
        'producto': producto,
    }
    return render(request, 'productos/detalle.html', context)


# Vista principal: catálogo inicial
def index(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "productos/index.html", {"productos": productos})


# Búsqueda avanzada en el catálogo
def catalogo(request):
    query = request.GET.get("q", "").strip()
    productos = Producto.objects.all()

    if query:
        filtros = (
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(precio__icontains=query)
        )
        productos = productos.filter(filtros)

    contexto = {
        "productos": productos,
        "busqueda": query
    }
    return render(request, "productos/index.html", contexto)


# Galería local
def galeria_local(request):
    ruta_img = os.path.join(settings.BASE_DIR, "productos", "static", "productos", "img")
    imagenes = []
    if os.path.exists(ruta_img):
        imagenes = [
            archivo for archivo in os.listdir(ruta_img)
            if archivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]
    return render(request, "productos/galeria.html", {"imagenes": imagenes})


# Agregar producto al carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.agregar(producto)
    return redirect('ver_carrito')


# Restar cantidad de un producto
def restar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.restar(producto)
    return redirect('ver_carrito')


# Eliminar producto del carrito por completo
def eliminar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.quitar(producto)
    return redirect('ver_carrito')


# Vaciar por completo el carrito
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

# Ver contenido del carrito
def ver_carrito(request):
    """
    Gestiona la vista del carrito.
    Maneja el UnicodeDecodeError limpiando la sesión del carrito si está corrupta.
    """
    try:
        carrito = Carrito(request)
        context = {'carrito': carrito}
    except UnicodeDecodeError:
        request.session.pop('carrito', None)
        return redirect('ver_carrito')
    return render(request, 'productos/carrito.html', context)











