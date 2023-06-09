import email
import random
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class Registro(models.Model):
    primer_nombre = models.CharField(max_length=100, default='Julian')
    segundo_nombre = models.CharField(max_length=100, blank=True, default='David')
    primer_apellido = models.CharField(max_length=100, default='Perdigon')
    segundo_apellido = models.CharField(max_length=100, blank=True, default='Rojas')
    tipo_documento = models.CharField(max_length=20, default='Cedula')
    numero_documento = models.CharField(max_length=50, default='1000593957')
    fecha_expedicion = models.DateField(default=timezone.now)
    fecha_nacimiento = models.DateField(default='2002-03-22')
    telefono_movil = models.CharField(max_length=20, default='3225123570')
    nacionalidad = models.CharField(max_length=100, default='Colombia')
    departamento_residencia = models.CharField(max_length=100, default='Bogota')
    ciudad_residencia = models.CharField(max_length=100, default='Bogota')
    direccion = models.CharField(max_length=200, default='Cra 3A #12-19')
    correo_electronico = models.EmailField(max_length=50, default='julianperdigon@usantotomas.edu.co')
    contrasena = models.CharField(max_length=50, default='Showtime435.')
    genero = models.CharField(max_length=10, choices=(('hombre', 'Hombre'), ('mujer', 'Mujer')), default='Hombre')
    codigo_referido = models.CharField(max_length=20, blank=True)
    acepto_notificaciones = models.BooleanField(default=False)
    acepto_terminos = models.BooleanField(default=False)
    banco = models.CharField(max_length=100, default='BBVA')
    id_usuario = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Apuestas(models.Model):
       apuesta1 = models.CharField(max_length=100, default='Julian')
       apuesta2 = models.CharField(max_length=100, blank=True, default='David') 

class IniciarSesion(models.Model):
    id_ini = models.ForeignKey(Registro, on_delete=models.CASCADE)
    username = models.EmailField(max_length=50, default='julianperdigon@usantotomas.edu.co')
    contrasena = models.CharField(max_length=50, default='Showtime435.')

class TarjetaCredito(models.Model):
    cc_number = models.CharField(max_length=50, default='123456789123')
    cc_name = models.CharField(max_length=50, default='Julian David Perdigon Rojas')
    contrasena = models.DateField(default='2023-05-10')
    cc_csc = models.CharField(max_length=3, default='123')
    id_TC = models.ForeignKey(Registro, on_delete=models.CASCADE)

class Perfil(models.Model):
    id_usuario = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    primer_nombre = models.CharField(max_length=100, default='Julian')
    segundo_nombre = models.CharField(max_length=100, blank=True, default='David')
    primer_apellido = models.CharField(max_length=100, default='Perdigon')
    segundo_apellido = models.CharField(max_length=100, blank=True, default='Rojas')
    fecha_nacimiento = models.DateField(default='2002-03-22')
    telefono_movil = models.CharField(max_length=20, default='3225123570')
    nacionalidad = models.CharField(max_length=100, default='Colombia')
    ciudad_residencia = models.CharField(max_length=100, default='Bogota')
    direccion = models.CharField(max_length=200, default='Cra 3A #12-19')
    correo_electronico = models.EmailField(max_length=50, default='julianperdigon@usantotomas.edu.co')
    genero = models.CharField(max_length=10, default='Hombre')
    banco = models.CharField(max_length=100, default='BBVA')
    num_cuenta = models.CharField(max_length=5, default=str(random.randint(10000, 99999)))
    banco = models.IntegerField(default=123456789)
    id_perfil = models.ForeignKey(Registro, on_delete=models.CASCADE)
    id_ini = models.ForeignKey(TarjetaCredito, on_delete=models.CASCADE)
    
class Admin(models.Model):
    id_administrator = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.EmailField(max_length=50, default='julianperdigon@usantotomas.edu.co')
    contrasena = models.CharField(max_length=50, default='Showtime435.')
    correo_electronico = models.EmailField(max_length=50, default='julianperdigon@usantotomas.edu.co')

class Eventos(models.Model):
    id_evento = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    nombre_evento = models.CharField(max_length=255, null=False)
    fecha_evento = models.DateField(null=False)
    hora_evento = models.TimeField(null=False)
    opcion_1 = models.CharField(max_length=255, null=False)
    opcion_1_prob = models.FloatField(null=False)
    opcion_2 = models.CharField(max_length=255, null=False)
    opcion_2_prob = models.FloatField(null=False)
    opcion_3 = models.CharField(max_length=255, null=False)
    opcion_3_prob = models.FloatField(null=False)
    ganadora = models.CharField(max_length=255, null=True, default=None)
    descripcion = models.TextField(null=True, default=None)
    administrador = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Apuesta(models.Model):
    OPCIONES_APUESTA = (
        ('opcion_1', 'Opción 1'),
        ('opcion_2', 'Opción 2'),
        ('opcion_3', 'Opción 3')
    )

    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    evento_apuesta = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    opcion_apuesta = models.CharField(max_length=50, choices=OPCIONES_APUESTA)
    monto_apuesta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)
    resultado_apuesta = models.CharField(max_length=50, blank=True, null=True)
    ganancia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)





