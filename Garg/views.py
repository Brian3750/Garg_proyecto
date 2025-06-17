from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import Agendamiento, Usuario
from .forms import UsuarioCreationForm  # <-- Asegúrate que este formulario exista

# Formulario de agendamiento
class AgendamientoForm(forms.ModelForm):
    class Meta:
        model = Agendamiento
        fields = ['nombre_paciente', 'rut', 'fecha', 'hora', 'direccion', 'servicio']

# Vista de inicio
def index(request):
    return render(request, 'Garg/index.html')

# Vista de servicios (genérica o resumen)
def servicios(request):
    return render(request, 'Garg/servicios.html')

# Vistas para servicios específicos
def servicio_telemedicina(request):
    return render(request, 'Garg/telemedicina.html')

def servicio_medicina_presencial(request):
    return render(request, 'Garg/medicina-presencial.html')

def servicio_medicina_mixta(request):
    return render(request, 'Garg/medicina-mixta.html')

def servicio_laboratorio(request):
    return render(request, 'Garg/laboratorio.html')

def servicio_enfermeria_examenes(request):
    return render(request, 'Garg/enfermeria-examenes.html')

def servicio_enfermeria_sondas(request):
    return render(request, 'Garg/enfermeria-sondas.html')

# Vista de agendamiento
def agendar(request):
    if request.method == 'POST':
        form = AgendamientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita agendada correctamente.")
            return redirect('index')
    else:
        form = AgendamientoForm()
    return render(request, 'Garg/agendamiento.html', {'form': form})

# Vista del panel administrativo (dashboard)
@login_required
def dashboard(request):
    if request.user.is_admin:
        agendamientos = Agendamiento.objects.all()
        return render(request, 'Garg/dashboard.html', {'agendamientos': agendamientos})
    else:
        return redirect('index')

# Vista de login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'Garg/login.html', {'form': form})

# Vista para cerrar sesión (logout)
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

# Vista para crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect('login')
    else:
        form = UsuarioCreationForm()
    return render(request, 'Garg/crear_usuario.html', {'form': form})
