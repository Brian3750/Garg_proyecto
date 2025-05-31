from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agendamiento
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Formulario de agendamiento
class AgendamientoForm(forms.ModelForm):
    class Meta:
        model = Agendamiento
        fields = ['nombre_paciente', 'rut', 'fecha', 'hora', 'direccion', 'servicio']

# Vista de inicio
def index(request):
    return render(request, 'Garg/index.html')

# Vista de servicios
def servicios(request):
    return render(request, 'Garg/servicios.html')

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

# Vista del panel administrativo
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
        form = AuthenticationForm()
    return render(request, 'Garg/login.html', {'form': form})

