from django.contrib import admin
from .models import CustomUser

# Registra tus modelos de la aplicación de usuarios aquí.
admin.site.register(CustomUser)