from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from . import models
# Create your views here.

def projects(request):
    return render(request, 'Registro.html')
def registro(request):
    if request.method == 'POST':
        primer_nombre = request.POST.get('primer_nombre')
        segundo_nombre = request.POST.get('segundo_nombre')
        numero_documento = request.POST.get('numero_documento')
        fecha_expedicion = request.POST.get('fecha_expedicion')

        user = models.Registro()
        user.is_active = 1
        user.numero_documento = numero_documento
        user.fecha_expedicion = fecha_expedicion
        user.primer_nombre = primer_nombre
        user.segundo_nombre = segundo_nombre

        user = User.objects.create_user(primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,numero_documento=numero_documento,fecha_expedicion=fecha_expedicion)

        user.save()
        return JsonResponse({'mensaje':'Se guardo'})
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
def Tarjeta(request):

    css_file = './templates/main.css'
    js_file = './templates/main.js'

    # Contexto de la plantilla con las rutas de los archivos CSS y JS
    context = {
        'css_file': css_file,
        'js_file': js_file
    }
    return render(request, 'pago.html' , context=context)
def Arsene(request):
    return render(request, 'Arsene.html')
    
