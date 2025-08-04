# productos/carrito.py

from decimal import Decimal
from django.conf import settings
from productos.models import Producto

class Carrito:
    """
    Clase para gestionar el carrito de compras del usuario, almacenado en la sesión.
    """
    def __init__(self, request):
        """
        Inicializa el carrito con el objeto de solicitud (request).
        """
        self.session = request.session
        # Obtener el carrito de la sesión o crear uno nuevo si no existe.
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def __iter__(self):
        """
        Itera sobre los ítems en el carrito y obtiene los objetos Producto de la base de datos.
        """
        producto_ids = self.carrito.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        
        carrito_copia = self.carrito.copy()
        for producto in productos:
            carrito_copia[str(producto.id)]['producto'] = producto
            
        for item in carrito_copia.values():
            item['precio'] = Decimal(item['precio'])
            item['total_item'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
        Retorna la cantidad total de ítems en el carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())

    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        """
        Agrega un producto al carrito o actualiza su cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                'cantidad': 0,
                'precio': str(producto.precio)
            }
        
        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        
        if self.carrito[producto_id]['cantidad'] <= 0:
            self.quitar(producto)
        self.guardar()

    def quitar(self, producto):
        """
        Elimina un producto del carrito.
        """
        producto_id = str(producto.id) if hasattr(producto, 'id') else str(producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def restar(self, producto):
        """
        Reduce la cantidad de un producto en 1. Lo elimina si la cantidad llega a 0.
        """
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] -= 1
            if self.carrito[producto_id]['cantidad'] <= 0:
                self.quitar(producto)
            self.guardar()

    def limpiar(self):
        """
        Elimina todos los productos del carrito.
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def guardar(self):
        """
        Marca la sesión como modificada para asegurar que se guarde.
        """
        self.session.modified = True

    def get_total_precio(self):
        """
        Calcula el precio total de todos los ítems en el carrito.
        """
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())

    def esta_vacio(self):
        """
        Verifica si el carrito está vacío.
        """
        return not bool(self.carrito)

    def total_productos_unicos(self):
        """
        Retorna la cantidad de productos únicos en el carrito.
        """
        return len(self.carrito)