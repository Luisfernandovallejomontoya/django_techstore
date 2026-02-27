from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta cargará el tablero de Filadelfia
    path('dashboard/', views.dashboard_suelos, name='dashboard_suelos'),
    
    # Ruta para el reporte individual del campesino
    path('alerta-campesino/', views.reporte_campesino, name='alerta_campesino'),
] # <--- Asegúrate de que este corchete esté ahí.
