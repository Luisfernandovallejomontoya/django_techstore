from django.shortcuts import render
from .models import RegistroSuelo

def dashboard_suelos(request):
    # Traemos todos los registros, del más nuevo al más viejo
    registros = RegistroSuelo.objects.all().order_by('-fecha')
    
    # Enviamos los datos a una plantilla HTML que crearemos después
    return render(request, 'agromaker_soil/dashboard.html', {'registros': registros})