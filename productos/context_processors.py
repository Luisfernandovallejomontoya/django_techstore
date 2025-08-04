# productos/context_processors.py

from .carrito import Carrito

def carrito_procesador(request):
    """
    Agrega la instancia del Carrito al contexto de todas las plantillas.
    Esto permite acceder a 'carrito.cantidad_total', 'carrito.get_total_precio'
    y 'carrito.total_productos_unicos' directamente en cualquier plantilla.
    """
    return {'carrito': Carrito(request)}


