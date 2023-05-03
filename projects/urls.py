from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('home/', views.Home, name="home"),
    path('pago/', views.Pago, name="formulario_de_pago"),
    path('iniciarsesion/', views.IniciarSesion, name="IniciarSesion"),
    path('TyC/', views.TyC, name="TerminosYCondiciones"),
]
