# productos/carrito.py

from decimal import Decimal # Importar para cálculos monetarios precisos
from django.conf import settings
from productos.models import Producto # Asegúrate de que este import sea correcto

class Carrito:
    """
    Clase para gestionar el carrito de compras del usuario, almacenado en la sesión.
    """
    def __init__(self, request):
        """
        Inicializa el carrito con el objeto de solicitud (request).
        """
        self.session = request.session
        # Obtener el carrito de la sesión o crear uno nuevo si no existe
        carrito = self.session.get(settings.CART_SESSION_ID) # Usar un ID de sesión configurable
        if not carrito:
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def __iter__(self):
        """
        Itera sobre los ítems en el carrito y obtiene los objetos Producto de la base de datos.
        """
        producto_ids = self.carrito.keys()
        # Obtener los objetos Producto y añadirle el carrito
        productos = Producto.objects.filter(id__in=producto_ids)
        
        carrito_copia = self.carrito.copy() # Trabajar con una copia para evitar modificar durante la iteración
        for producto in productos:
            carrito_copia[str(producto.id)]['producto'] = producto # Añade el objeto Producto
            
        for item in carrito_copia.values():
            item['precio'] = Decimal(item['precio']) # Convertir precio a Decimal
            item['total_item'] = item['precio'] * item['cantidad'] # Calcular total por ítem
            yield item # Retorna un generador para iterar eficientemente

    def __len__(self):
        """
        Retorna la cantidad total de ítems distintos en el carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())

    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        """
        Agrega un producto al carrito o actualiza su cantidad.
        :param producto: Objeto Producto (no solo el ID).
        :param cantidad: Cantidad a añadir.
        :param actualizar_cantidad: Si es True, la cantidad se establecerá, no se sumará.
        """
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                'cantidad': 0, # Inicializar cantidad en 0 antes de sumar
                'precio': str(producto.precio)
            }
        
        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
            
        # Asegurarse de que la cantidad no sea negativa
        if self.carrito[producto_id]['cantidad'] <= 0:
            self.quitar(producto) # Eliminar si la cantidad llega a cero o menos

        self.guardar()

    def quitar(self, producto):
        """
        Elimina un producto del carrito.
        :param producto: Objeto Producto o su ID.
        """
        producto_id = str(producto.id) if hasattr(producto, 'id') else str(producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
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
        Calcula el precio total de los ítems en el carrito.
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
