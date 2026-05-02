from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RegistroSuelo
from .semaforo import evaluar_estado_suelo
from xhtml2pdf import pisa

def reporte_campesino(request):
    """
    Vista principal del Monitor de Suelos.
    Muestra tarjetas de registros + alerta del semáforo.
    El formulario de registro está integrado en el template.
    """
    ultimo_registro = RegistroSuelo.objects.all().order_by('-fecha').first()
    todos_los_registros = RegistroSuelo.objects.all().order_by('-fecha')
    est = evaluar_estado_suelo(ultimo_registro)

    contexto = {
        'registro': ultimo_registro,
        'registros': todos_los_registros,
        'alerta': est.alerta,
        'recomendacion': est.recomendacion,
        'color': est.color,
        'color_hex': est.color_hex,
        'municipio': 'Filadelfia, Caldas',
        'status_ceo': "ACTIVO SOBERANO - AGROMAKER AI"
    }

    return render(request, 'agromaker_soil/dashboard.html', contexto)

def dashboard_suelos(request):
    """Alias para compatibilidad."""
    return reporte_campesino(request)

import logging

logger = logging.getLogger(__name__)

def registrar_dato(request):
    """
    Recibe POST del formulario.
    Valida, hace CLAMP (0-100) para evitar datos imposibles (>100%),
    y registra con log de depuración.
    """
    if request.method == "POST":
        lote_nombre = request.POST.get('lote', 'San Bernardo, Filadelfia')
        ph_raw = request.POST.get('ph', '0')
        h_raw = request.POST.get('humedad', '0')
        cond_raw = request.POST.get('conductividad', '')

        ph_limpio = ph_raw.replace(',', '.')
        h_limpio = h_raw.replace(',', '.')

        try:
            ph_num = float(ph_limpio)
            h_num = float(h_limpio)
        except ValueError:
            messages.error(request, "Valores numéricos inválidos para pH o humedad.")
            return redirect('agromaker_soil:reporte_campesino')

        # 🔒 CLAMP DE SEGURIDAD: La humedad física no puede ser >100% ni <0%
        h_original = h_num
        h_num = max(0.0, min(100.0, h_num))
        
        if h_original != h_num:
            logger.warning(f"⚠️ Humedad fuera de rango recibida: {h_original}%. Ajustada a {h_num}%.")
            messages.warning(request, f"Humedad ajustada de {h_original}% a {h_num}% (límite físico).")

        # Validar pH
        ph_num = max(0.0, min(14.0, ph_num))

        # Log de depuración en consola
        print(f"📡 POST RECIBIDO — Lote: {lote_nombre} | pH: {ph_raw} → {ph_num} | Hum: {h_raw} → {h_num}")

        conductividad = None
        if cond_raw.strip():
            try:
                conductividad = float(str(cond_raw).replace(',', '.'))
            except (ValueError, TypeError):
                conductividad = h_num

        RegistroSuelo.objects.create(
            lote=lote_nombre,
            ph=ph_num,
            humedad=h_num,
            conductividad=conductividad or h_num,
            observaciones="Sincronización Automática — Nodo Filadelfia"
        )

        messages.success(request, f"✅ Registro guardado: {lote_nombre} — pH {ph_num} | Hum {h_num}%")
        return redirect('agromaker_soil:reporte_campesino')

    return redirect('agromaker_soil:reporte_campesino')

def exportar_pdf_suelo(request):
    """Genera certificado PDF oficial."""
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
