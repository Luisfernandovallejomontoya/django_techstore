from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from .models import Pedido, DetallePedido
from django.contrib import messages
from django.db import transaction

# Create your views here.
@login_required
def crear_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('catalogo')

    try:
        with transaction.atomic():
            pedido = Pedido.objects.create(user=request.user)

            for producto_id, item_data in carrito.items():
                producto = Producto.objects.get(id=producto_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=item_data['cantidad'],
                    precio_total=item_data['acumulado']
                )

            request.session['carrito'] = {}
            messages.success(request, f"Tu pedido #{pedido.id} ha sido creado con éxito.")
            return redirect('catalogo')

    except Exception as e:
        messages.error(request, f"Ocurrió un error al procesar tu pedido: {e}")
        return redirect('catalogo')
