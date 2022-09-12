from django.db import models

# Create your models here.
class compania(models.Model):
    nombreCompania=models.CharField(max_length=50, primary_key=True)
    

class usuario(models.Model):
    name=models.CharField(max_length=60, primary_key=True)
    apellido=models.CharField(max_length=30, null=True)
    usuario=models.CharField(max_length=30, null=True)
    correo=models.CharField(max_length=30, null=True)
    constraseña=models.CharField(max_length=20, null=True)
    nombreCompania=models.OneToOneField(compania, on_delete=models.CASCADE)

class producto(models.Model):
    nombreProducto=models.CharField(max_length=60, primary_key=True)
    tipoProducto=models.CharField(max_length=30)
    cantidadProducto=models.IntegerField()
    def __str__(self):
        return self.nombreProducto

    
