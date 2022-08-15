from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=120)
    usuario = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
