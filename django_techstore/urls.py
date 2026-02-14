from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Todo lo de IA se maneja dentro de su propio archivo de rutas
    path('agromaker-ai/', include('agromaker_ai.urls')), 
    
    # E-commerce
    path('productos/', include('productos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('pedidos/', include('pedidos.urls')),
    
    # Inicio
    path('', include('productos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)