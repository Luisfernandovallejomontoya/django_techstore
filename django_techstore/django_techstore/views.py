from django.shortcuts import render
from productos.models import Producto

def home_view(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'index.html', contexto)