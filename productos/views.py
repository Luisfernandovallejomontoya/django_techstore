# productos/views.py

import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db import transaction
from django.urls import reverse

# Importamos los modelos necesarios
from .models import Producto, Pedido, DetallePedido
from .carrito import Carrito

# ==========================================
# 🏠 VISTA DEL HUB AGROMAKER (NUEVA)
# ==========================================
def hub_agromaker(request):
    """
    Punto de entrada principal del sistema.
    Muestra el panel con acceso a Suelos e IA Satelital.
    """
    return render(request, 'hub_agromaker.html')

# ==========================================
# 🏬 VISTAS DEL CATÁLOGO Y DETALLE
# ==========================================

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    context = {
        'producto': producto,
    }
    return render(request, 'productos/detalle.html', context)

def index(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "productos/index.html", {"productos": productos})

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

# ==========================================
# 🖼️ GALERÍA LOCAL
# ==========================================

def galeria_local(request):
    ruta_img = os.path.join(settings.BASE_DIR, "productos", "static", "productos", "img")
    imagenes = []
    if os.path.exists(ruta_img):
        imagenes = [
            archivo for archivo in os.listdir(ruta_img)
            if archivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]
    return render(request, "productos/galeria.html", {"imagenes": imagenes})

# ==========================================
# 🛒 LÓGICA DEL CARRITO (CLASE CARRITO)
# ==========================================

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.agregar(producto)
    return redirect('ver_carrito')

def restar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.restar(producto)
    return redirect('ver_carrito')

def eliminar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.quitar(producto)
    return redirect('ver_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def ver_carrito(request):
    try:
        carrito = Carrito(request)
        context = {'carrito': carrito}
    except UnicodeDecodeError:
        request.session.pop('carrito', None)
        return redirect('ver_carrito')
    return render(request, 'productos/carrito.html', context)

# ==========================================
# 📦 PROCESAMIENTO DE PEDIDOS
# ==========================================

def procesar_pedido(request):
    if request.user.is_authenticated:
        carrito = Carrito(request)
        productos_carrito = carrito.get_products_in_cart()
        
        if not productos_carrito:
            return redirect('ver_carrito')
        
        try:
            with transaction.atomic():
                # 1. Crear el objeto Pedido
                pedido = Pedido.objects.create(
                    user=request.user,
                    total=carrito.get_total_price()
                )

                # 2. Iterar sobre el carrito para crear los DetallePedido
                for item in productos_carrito:
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=item['producto'],
                        cantidad=item['cantidad'],
                        precio_unitario=item['precio']
                    )
            
            # 3. Vaciar el carrito después de guardar el pedido
            carrito.limpiar()
            return render(request, 'productos/confirmacion_pedido.html')

        except Exception as e:
            print(f"Error al procesar el pedido: {e}")
            return redirect('ver_carrito')
    else:
        return redirect('login')