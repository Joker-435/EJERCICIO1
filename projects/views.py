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