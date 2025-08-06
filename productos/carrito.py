# productos/carrito.py

from decimal import Decimal
from django.conf import settings
from productos.models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                'producto_id': producto_id,
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'imagen': producto.imagen.url,
                'cantidad': 1,
                'acumulado': float(producto.precio),
            }
        else:
            self.carrito[producto_id]['cantidad'] += 1
            self.carrito[producto_id]['acumulado'] += float(producto.precio)
        self.guardar()

    def restar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] -= 1
            self.carrito[producto_id]['acumulado'] -= float(producto.precio)
            if self.carrito[producto_id]['cantidad'] == 0:
                self.quitar(producto)
            self.guardar()

    def quitar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def limpiar(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.guardar()

    def guardar(self):
        self.session.modified = True

    @property
    def items(self):
        return self.carrito.items()
    
    @property
    def total_acumulado(self):
        # Usamos .get para manejar de forma segura los valores que no tienen la clave 'acumulado'
        total = sum(item.get('acumulado', 0) for item in self.carrito.values())
        return total

    def __iter__(self):
        for item in self.carrito.values():
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())