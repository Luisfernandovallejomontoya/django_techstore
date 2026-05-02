# productos/context_processors.py

from .carrito import Carrito

def carrito_procesador(request):
    """
    Agrega la instancia del Carrito al contexto de todas las plantillas.
    Maneja sesiones corruptas de forma segura.
    """
    try:
        return {'carrito': Carrito(request)}
    except Exception:
        # Si la sesión está corrupta, limpiamos y retornamos carrito vacío
        try:
            request.session['carrito'] = {}
        except Exception:
            pass
        return {'carrito': None}


