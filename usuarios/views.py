from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import FormularioLogin
from django.contrib import messages

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, "¡Registrado Correctamente!")
            return redirect('productos:catalogo')
        else:
            messages.error(request, "Error al registrar. Por favor, revisa los datos.")
    else:
        form = UserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = FormularioLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"¡Bienvenido de vuelta, {username}!")
                return redirect("productos:catalogo")
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Información inválida")

    form = FormularioLogin()
    return render(request, "usuarios/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect("productos:catalogo")
