from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.db.models import Q
from productos.models import Producto

# 🧮 Vista de detalle: muestra información del producto + aplica filtro 'multiply'
def detalle_producto(request, producto_id):
    # ✅ Corrección: uso correcto de get_object_or_404
    producto = get_object_or_404(Producto, pk=producto_id)
    cantidad = 3  # 🔧 Puedes cambiar esto según contexto dinámico (carrito, input, etc.)

    context = {
        'producto': producto,
        'cantidad': cantidad,
    }
    return render(request, 'productos/detalle.html', context)


# 🏬 Vista principal: catálogo inicial
def index(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "productos/index.html", {"productos": productos})


# 🔍 Búsqueda avanzada en el catálogo
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


# 🖼️ Galería local sin base de datos
def galeria_local(request):
    ruta_img = os.path.join(settings.BASE_DIR, "productos", "static", "productos", "img")
    imagenes = []

    if os.path.exists(ruta_img):
        imagenes = [
            archivo for archivo in os.listdir(ruta_img)
            if archivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]

    return render(request, "productos/galeria.html", {"imagenes": imagenes})


# 🛒 Ver contenido del carrito
def ver_carrito(request):
    carrito = request.session.get("carrito", {})
    productos_en_carrito = []

    for producto_id, datos in carrito.items():
        try:
            producto = Producto.objects.get(pk=producto_id)
            productos_en_carrito.append({
                "producto": producto,
                "cantidad": datos["cantidad"]
            })
        except Producto.DoesNotExist:
            continue

    return render(request, "productos/carrito.html", {"carrito": productos_en_carrito})


# ➕ Agregar producto al carrito
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get("carrito", {})
    producto = get_object_or_404(Producto, pk=producto_id)
    clave = str(producto_id)

    if clave in carrito:
        carrito[clave]["cantidad"] += 1
    else:
        carrito[clave] = {
            "cantidad": 1,
            "precio": str(producto.precio)
        }

    request.session["carrito"] = carrito
    request.session.modified = True
    return redirect("ver_carrito")


# 🗑️ Eliminar producto del carrito
def quitar_del_carrito(request, producto_id):
    carrito = request.session.get("carrito", {})
    clave = str(producto_id)

    if clave in carrito:
        del carrito[clave]
        request.session["carrito"] = carrito
        request.session.modified = True

    return redirect("ver_carrito")


# 🔼 Aumentar cantidad de un producto
def aumentar_cantidad(request, producto_id):
    carrito = request.session.get("carrito", {})
    clave = str(producto_id)

    if clave in carrito:
        carrito[clave]["cantidad"] += 1
        request.session["carrito"] = carrito
        request.session.modified = True

    return redirect("ver_carrito")


# 🔽 Reducir cantidad de un producto (hasta eliminar)
def reducir_cantidad(request, producto_id):
    carrito = request.session.get("carrito", {})
    clave = str(producto_id)

    if clave in carrito:
        if carrito[clave]["cantidad"] > 1:
            carrito[clave]["cantidad"] -= 1
        else:
            del carrito[clave]

        request.session["carrito"] = carrito
        request.session.modified = True

    return redirect("ver_carrito")


# 🧹 Vaciar por completo el carrito
def limpiar_carrito(request):
    if "carrito" in request.session:
        del request.session["carrito"]
        request.session.modified = True

    return redirect("ver_carrito")












































































































































