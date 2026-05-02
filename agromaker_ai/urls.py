from django.urls import path
from . import views

app_name = 'agromaker_ai'

urlpatterns = [
    # Esta es la ruta que te faltaba y causaba el error NoReverseMatch
    path('guardar-semaforo/', views.guardar_semaforo, name='guardar_semaforo'), 
    
    path('semaforo/', views.semaforo_ia, name='semaforo_ia'), 
    
    # IMPORTANTE: Cambia 'dashboard_ia' por 'estado_campo' para que coincida con tu redirect
    path('dashboard/', views.estado_campo, name='estado_campo'), 
    
    path('mapa-satelital/', views.mapa_completo, name='mapa_completo'),
    path('exportar/', views.exportar_excel, name='exportar_excel'),
]