from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta cargará el tablero de Filadelfia
    path('dashboard/', views.dashboard_suelos, name='dashboard_suelos'),
]
