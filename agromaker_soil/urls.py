from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta cargará el tablero general de Filadelfia
    path('dashboard/', views.dashboard_suelos, name='dashboard_suelos'),
    
    # Ruta para el reporte individual del campesino (El semáforo IA)
    path('alerta-campesino/', views.reporte_campesino, name='reporte_campesino'),

    # NUEVA: Ruta para el ingreso de datos manual o desde sensor (Activos subsidiados)
    path('registrar/', views.registrar_dato, name='registrar_dato'),
]