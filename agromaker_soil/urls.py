from django.urls import path
from . import views

app_name = 'agromaker_soil'

urlpatterns = [
    path('', views.reporte_campesino, name='reporte_campesino'),
    path('dashboard/', views.dashboard_suelos, name='dashboard_suelos'),
    path('registrar/', views.registrar_dato, name='registrar_dato'),
    path('exportar-pdf/', views.exportar_pdf_suelo, name='exportar_pdf'),
]