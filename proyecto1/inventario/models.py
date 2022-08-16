from django.db import models

# Create your models here.
class compania(models.Model):
    nombreCompania=models.CharField(max_length=50, null=True)
    

class usuario(models.Model):
    name=models.CharField(max_length=60, null=True)
    apellido=models.CharField(max_length=30, null=True)
    usuario=models.CharField(max_length=30, null=True)
    correo=models.CharField(max_length=30, null=True)
    constraseña=models.CharField(max_length=20, null=True)
    nombreCompania=models.OneToOneField(compania, on_delete=models.CASCADE, primary_key=True)

class producto(models.Model):
    nombreProducto=models.CharField(max_length=60, null=True)
    tipoProducto=models.IntegerField()
    cantidadProducto=models.IntegerField()

    
