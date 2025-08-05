from django.shortcuts import render
from django.http import HttpResponse

# Crea tus vistas aquí.
def login_view(request):
    return HttpResponse("Esta es la página de inicio de sesión de usuarios.")

def registro(request):
    if request.method == 'POST':
        # Aquí procesaremos los datos del formulario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Datos recibidos: Nombre de usuario: {username}, Correo: {email}, Contraseña: {password}")

    return render(request, 'usuarios/registro.html', {})