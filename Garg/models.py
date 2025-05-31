from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuario personalizado
class Usuario(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name="Administrador")
    is_profesional = models.BooleanField(default=False, verbose_name="Profesional de Salud")

    # Añadimos related_name para evitar el conflicto con auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='garg_usuario_set', # Nombre único para el reverse accessor
        related_query_name='garg_usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='garg_usuario_permissions', # Nombre único para el reverse accessor
        related_query_name='garg_usuario',
    )

    def __str__(self):
        return f"{self.username} ({'Admin' if self.is_admin else 'Profesional'})"

# Modelo de agendamiento de atención médica
class Agendamiento(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, help_text="Formato: 12.345.678-9")
    fecha = models.DateField()
    hora = models.TimeField()
    direccion = models.CharField(max_length=255)
    servicio = models.CharField(max_length=100, help_text="Ej: Enfermería, Kinesiología, etc.")
    profesional = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_profesional': True})
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_paciente} - {self.fecha.strftime('%d/%m/%Y')} {self.hora.strftime('%H:%M')}"

    class Meta:
        verbose_name = "Agendamiento"
        verbose_name_plural = "Agendamientos"
        ordering = ['-fecha', '-hora']