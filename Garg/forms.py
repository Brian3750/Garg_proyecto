from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Si tienes un modelo personalizado

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario  # O `User` si usas el modelo por defecto
        fields = ['username', 'email', 'first_name', 'last_name']
