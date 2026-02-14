from django.urls import path
from . import views

app_name = 'agromaker_ai'

urlpatterns = [
    # 1. El Semáforo interactivo (El diseño que te gusta)
    path('semaforo/', views.semaforo_ia, name='semaforo_ia'), 
    
    # 2. El Dashboard técnico (Donde está el EXCEL y las 7 filas)
    path('dashboard/', views.estado_campo, name='dashboard_ia'), 
    
    # 3. El Mapa
    path('mapa-satelital/', views.mapa_completo, name='mapa_completo'),
    
    # 4. El botón de exportar Excel
    path('exportar/', views.exportar_excel, name='exportar_excel'),
]