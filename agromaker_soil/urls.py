from django.urls import path
from . import views

urlpatterns = [
    # 1. Monitor Principal (El semáforo IA que ya logramos estabilizar)
    # Lo dejamos como ruta principal ('') para que cargue al entrar a la app
    path('', views.reporte_campesino, name='reporte_campesino'),

    # 2. Historial Técnico para Auditoría (Fondo 305 CEO)
    path('dashboard/', views.dashboard_suelos, name='dashboard_suelos'),

    # 3. Registro de datos (Entrada desde tablet o sensor)
    path('registrar/', views.registrar_dato, name='registrar_dato'),

    # 4. EXPORTACIÓN OFICIAL (NUEVA: Para el certificado PDF)
    path('exportar-pdf/', views.exportar_pdf_suelo, name='exportar_pdf'),
]