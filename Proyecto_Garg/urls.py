from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Garg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/telemedicina/', views.servicio_telemedicina, name='servicio_telemedicina'),
    path('servicios/medicina-presencial/', views.servicio_medicina_presencial, name='servicio_medicina_presencial'),
    path('servicios/medicina-mixta/', views.servicio_medicina_mixta, name='servicio_medicina_mixta'),
    path('servicios/laboratorio/', views.servicio_laboratorio, name='servicio_laboratorio'),
    path('servicios/enfermeria-examenes/', views.servicio_enfermeria_examenes, name='servicio_enfermeria_examenes'),
    path('servicios/enfermeria-sondas/', views.servicio_enfermeria_sondas, name='servicio_enfermeria_sondas'),
    path('agendamiento/', views.agendar, name='agendamiento'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

# Archivos estáticos y multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
