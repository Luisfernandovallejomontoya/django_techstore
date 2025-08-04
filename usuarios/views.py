# usuarios/views.py
from django.shortcuts import render

def registro(request):
    # Por ahora, solo renderizaremos una plantilla básica
    return render(request, 'usuarios/registro.html', {})

