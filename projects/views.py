from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def projects(request):
    return render(request, 'Registro.html')
def registro(request):
    if request.method == 'POST':
        numero_documento = request.POST['numero_documento']
        fecha_expedicion = request.POST['fecha_expedicion']

        user = models.Projects()
        user.is_active = 1
        user.numero_documento = numero_documento
        user.fecha_expedicion = fecha_expedicion
        user.save()
    return render(request, 'Registro.html')
def Home(request):
    return render(request, 'home.html' )
def Pago(request):
    return render(request,'formulario_de_pago.html')
def IniciarSesion(request):
    return render(request, 'IniciarSesion.html')
def TyC(request):
    return render(request, 'TerminosYCondiciones.html')
def Baloncesto(request):
    return render(request, 'Comp_balo.html')
def Competencias(request):
    return render(request, 'Competencias.html')
def Futbol(request):
    return render(request, 'Compt_Futbol.html')
def Perfil(request):
    return render(request, 'perfil-1.html')