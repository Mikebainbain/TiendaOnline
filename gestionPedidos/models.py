from django.db import models

# Create your models here.

class clientes(models.Model):
    
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Almacen(models.Model):
    nombre = models.CharField(max_length=60)
    lugar = models.IntegerField()

class Pedidos(models.Model):
    folio = models.IntegerField()
    fecha = models.DateField()
    entrregado = models.BooleanField()