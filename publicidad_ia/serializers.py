# publicidad_ia/serializers.py

from rest_framework import serializers
from .models import CampanaPublicitaria, Anuncio

# **IMPORTANTE:** Necesitamos hacer referencia al ProductoSerializer
# que se encuentra en tu aplicación 'productos' (la de los productos tecnológicos).
# Por ahora, asumiremos una estructura estándar. Si esta línea causa un error
# porque 'productos/serializers.py' no existe, te pediré que lo crees después
# o que comentes la línea 'producto = ProductoSerializer(...)'.

try:
    # Intenta importar el ProductoSerializer de tu app 'productos'
    from productos.serializers import ProductoSerializer
except ImportError:
    # Define una clase stub (vacía) para evitar errores si el archivo aún no existe
    # o si quieres un Serializer simple que solo muestre el ID del producto
    class ProductoSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        nombre = serializers.CharField(read_only=True)


class CampanaPublicitariaSerializer(serializers.ModelSerializer):
    """Serializer para el modelo CampanaPublicitaria."""
    class Meta:
        model = CampanaPublicitaria
        fields = '__all__' # Incluye todos los campos del modelo


class AnuncioSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Anuncio."""
    
    # Campo anidado: Muestra los detalles del producto tecnológico asociado
    # en lugar de solo su ID. Usa el ProductoSerializer importado (o el stub).
    producto = ProductoSerializer(read_only=True) 
    
    class Meta:
        model = Anuncio
        fields = '__all__'
        # Campos de solo lectura si solo queremos exponerlos y no permitir que se modifiquen
        # read_only_fields = ('fecha_creacion',)