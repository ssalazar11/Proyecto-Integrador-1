from django.db import models

# Create your models here.

class usuario(models.Model):
    name=models.CharField(max_length=60)
    nombreCompania=models.CharField(max_length=60, null=True)

class compania(models.Model):
    nombreCompania=models.OneToOneField(usuario, on_delete=models.CASCADE, primary_key=True)

class producto(models.Model):
    nombreProducto=models.CharField(max_length=60)
    tipoProducto=models.IntegerField()
    cantidadProducto=models.IntegerField()

    
