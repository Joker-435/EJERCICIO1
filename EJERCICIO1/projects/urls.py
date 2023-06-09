from django.urls import path
from . import views


urlpatterns = [
    path('', views.Arsene, name="Arsene"),
    path('projects/', views.projects, name="projects"),
    path('home/', views.Home, name="home"),
    path('pago/', views.Pago, name="formulario_de_pago"),
    path('iniciarsesion/', views.IniciarSesion, name="IniciarSesion"),
    path('TyC/', views.TyC, name="TerminosYCondiciones"),
    path('Baloncesto/', views.Baloncesto, name="Baloncesto"),
    path('Competencias/', views.Competencias, name="Competencias"),
    path('Futbol/', views.Futbol, name="Futbol"),
    path('Perfil/', views.Perfil, name="Perfil"),
    path('Tarjeta/', views.Tarjeta, name="Tarjeta")
]
