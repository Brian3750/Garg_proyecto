from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Agendamiento

# Personalización del panel para el modelo Usuario
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'is_admin', 'is_profesional', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Roles de usuario', {'fields': ('is_admin', 'is_profesional')}),
    )

# Registro de los modelos en el panel admin
admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Agendamiento)
