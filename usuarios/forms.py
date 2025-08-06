from django.contrib.auth.forms import AuthenticationForm
from django import forms

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}))