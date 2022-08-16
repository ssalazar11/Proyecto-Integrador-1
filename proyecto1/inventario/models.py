from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=120)
    usuario = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

class compania(models.Model):
    nombreCompania = models.OneToOneField(usuario, on_delete=models.CASCADE,primary_key = True)

class producto(models.Model):
    nombreProducto = models.CharField(max_length=60, null= True)
    tipoProducto = models.IntegerField()
    cantidadProducto = models.IntegerField()
