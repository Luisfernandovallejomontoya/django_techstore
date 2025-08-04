# django_techstore/urls.py

"""
URL configuration for django_techstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# --- ¡NUEVAS IMPORTACIONES AÑADIDAS AQUÍ! ---
from django.conf import settings
from django.conf.urls.static import static
# --------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),  # Include URLs from the productos app
]

# Configuración para servir archivos multimedia y estáticos en modo DEBUG (desarrollo)
# ¡IMPORTANTE!: Esto SOLO funciona en modo DEBUG (desarrollo).
# En producción, un servidor web como Nginx o Apache se encargará de esto.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Esta línea asegura que el servidor de desarrollo sirva los archivos estáticos.
    # Es una buena práctica añadirla, aunque Django a menudo lo hace por defecto.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
