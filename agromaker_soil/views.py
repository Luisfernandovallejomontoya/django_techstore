from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import RegistroSuelo
from xhtml2pdf import pisa # Importación para los certificados

def dashboard_suelos(request):
    """ Historial técnico completo para auditoría de activos (Fondo 305 CEO) """
    registros = RegistroSuelo.objects.all().order_by('-fecha')
    return render(request, 'agromaker_soil/dashboard.html', {'registros': registros})

def reporte_campesino(request):
    """ Lógica de IA: Semáforo pedagógico para Filadelfia """
    ultimo_registro = RegistroSuelo.objects.last()
    todos_los_registros = RegistroSuelo.objects.all().order_by('-fecha')
    
    alerta = "ESTADO ÓPTIMO"
    recomendacion = "Puede proceder con las labores programadas."
    color = "verde"

    if ultimo_registro:
        val_humedad = getattr(ultimo_registro, 'conductividad', 0)
        try:
            val_humedad_num = float(str(val_humedad).replace(',', '.')) if val_humedad else 0
            val_ph_num = float(str(ultimo_registro.ph).replace(',', '.')) if ultimo_registro.ph else 7.0
        except (ValueError, TypeError):
            val_humedad_num = 0
            val_ph_num = 7.0
        
        if val_ph_num < 5.5:
            alerta = "ALERTA DE ACIDEZ"
            recomendacion = "Aplicar enmienda (cal agrícola) para corregir el pH."
            color = "rojo"
        elif val_humedad_num > 80:
            alerta = "SATURACIÓN POR LLUVIA"
            recomendacion = "SUSPENDER FERTILIZACIÓN. Suelo saturado, riesgo de lixiviación."
            color = "naranja"

    contexto = {
        'registro': ultimo_registro,
        'registros': todos_los_registros, 
        'alerta': alerta,
        'recomendacion': recomendacion,
        'color': color,
        'municipio': 'Filadelfia, Caldas'
    }
    return render(request, 'agromaker_soil/dashboard.html', contexto)

def registrar_dato(request):
    """ Inyector de datos: Mapea la entrada 'humedad' a la columna 'conductividad' """
    if request.method == "POST":
        lote_nombre = request.POST.get('lote')
        ph_valor = request.POST.get('ph')
        h_val = request.POST.get('humedad') 

        if ph_valor: ph_valor = ph_valor.replace(',', '.')
        if h_val: h_val = h_val.replace(',', '.')

        RegistroSuelo.objects.create(
            lote=lote_nombre,
            ph=ph_valor,
            conductividad=h_val, 
            observaciones=f"Activo Subsidiado - Sincronización Filadelfia"
        )
        return redirect('reporte_campesino') 
    
    return render(request, 'agromaker_soil/registrar.html')

def exportar_pdf_suelo(request):
    """ Genera certificado oficial con respaldo del Fondo 305 CEO """
    ultimo_registro = RegistroSuelo.objects.last()
    
    contexto = {
        'registro': ultimo_registro,
        'municipio': 'Filadelfia, Caldas',
        'status_ceo': "ACTIVO SUBSIDIADO - FONDO 305 CEO"
    }
    
    template = get_template('agromaker_soil/pdf_template.html')
    html = template.render(contexto)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Certificado_Agromaker_CEO.pdf"'
    
    # Creación del PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error al generar el certificado técnico', status=500)
    return response