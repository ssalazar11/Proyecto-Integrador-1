from django.db import models

# Create your models here.

class Producto(models.Model):
    Categoria = models.ForeignKey(
        "Categoria", on_delete=models.CASCADE)
    Empresa = models.ForeignKey(
    "Empresa", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.IntegerField()
    Precio = models.FloatField()


class Categoria(models.Model):
    Nombre = models.CharField(max_length=20)

    
class Empresa(models.Model):
    Nombre = models.CharField(max_length=20)

class Usuario(models.Model):
    Empresa = models.ForeignKey(
        "Empresa", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Correo = models.EmailField()
    Password = models.CharField()

class Venta(models.Model):
    Cliente = models.ForeignKey(
    "Cliente", on_delete=models.CASCADE)
    
    Nombre = models.CharField(max_length=20)
    Cantidad = models.IntegerField()
    Precio = models.FloatField()
