# C:\Users\Administrador\Desktop\TechStoreOneline\django_techstore\django_techstore\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include('productos.urls')),
    path('pedidos/', include('pedidos.urls')), # ¡Esta es la línea que faltaba!
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)