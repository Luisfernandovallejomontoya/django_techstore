from django.shortcuts import render, redirect  # <--- IMPORTANTE: Aquí añadimos 'redirect'
from django.http import HttpResponse
from django.template.loader import get_template
from .models import RegistroSuelo
from .semaforo import evaluar_estado_suelo
from xhtml2pdf import pisa

def reporte_campesino(request):
    """
    Vista principal del Dashboard. 
    Usa el 'Juez' (semaforo.py) para garantizar coherencia total.
    """
    # 1. Obtener datos
    ultimo_registro = RegistroSuelo.objects.all().order_by('-fecha').first()
    todos_los_registros = RegistroSuelo.objects.all().order_by('-fecha')
    
    # 2. Consultar al Juez (Incluso si no hay registros, el semáforo maneja el None)
    est = evaluar_estado_suelo(ultimo_registro)

    # 3. Construir contexto único para evitar lógica en el HTML
    contexto = {
        'registro': ultimo_registro,
        'registros': todos_los_registros,
        'alerta': est.alerta,
        'recomendacion': est.recomendacion,
        'color': est.color,          # Para clases de Bootstrap (warning, danger)
        'color_hex': est.color_hex,  # Para estilos CSS precisos
        'municipio': 'Filadelfia, Caldas',
        'status_ceo': "ACTIVO SOBERANO - AGROMAKER AI"
    }
    
    return render(request, 'agromaker_soil/dashboard.html', contexto)

def dashboard_suelos(request):
    """ 
    Alias para mantener compatibilidad con otras rutas de la auditoría.
    Redirige a la lógica unificada de reporte_campesino.
    """
    return reporte_campesino(request)

def registrar_dato(request):
    """
    Inyector de datos con normalización de decimales.
    Asegura que '5,4' se convierta en '5.4' antes de guardar.
    """
    if request.method == "POST":
        lote_nombre = request.POST.get('lote', 'Filadelfia - Lote Principal')
        ph_raw = request.POST.get('ph', '0')
        h_raw = request.POST.get('humedad', '0') 

        # Normalización técnica: cambio de coma por punto
        ph_limpio = ph_raw.replace(',', '.')
        h_limpio = h_raw.replace(',', '.')

        try:
            ph_num = float(ph_limpio)
            h_num = float(h_limpio)
        except ValueError:
            ph_num = 0.0
            h_num = 0.0

        # Creación del registro en la base de datos soberana
        RegistroSuelo.objects.create(
            lote=lote_nombre,
            ph=ph_num,
            humedad=h_num,
            conductividad=h_num, # Sincronización para compatibilidad de sensores
            observaciones="Sincronización Automática - Filadelfia Nodo Caldas"
        )
        return redirect('reporte_campesino') 
    
    return render(request, 'agromaker_soil/registrar.html')

def exportar_pdf_suelo(request):
    """ 
    Genera certificado oficial con la misma lógica del semáforo.
    """
    ultimo_registro = RegistroSuelo.objects.all().order_by('-fecha').first()
    est = evaluar_estado_suelo(ultimo_registro)
    
    contexto = {
        'registro': ultimo_registro,
        'estado': est,
        'municipio': 'Filadelfia, Caldas',
        'status_ceo': "ACTIVO SUBSIDIADO - FONDO 305 CEO"
    }
    
    template = get_template('agromaker_soil/pdf_template.html')
    html = template.render(contexto)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Tecnico_Agromaker.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error técnico al generar certificado', status=500)
    return response