from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productos.views import hub_agromaker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hub_agromaker, name='hub_principal'),
    path('productos/', include(('productos.urls', 'productos'), namespace='productos')),
    path('usuarios/', include('usuarios.urls')),
    path('agromaker/', include('agromaker_ai.urls')),
    path('suelos/', include(('agromaker_soil.urls', 'agromaker_soil'), namespace='agromaker_soil')),
    path('pedidos/', include('pedidos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)