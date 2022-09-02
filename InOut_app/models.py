from django.db import models

# Create your models here.

class Producto(models.Model):
    Categoria = models.ForeignKey(
        "Categoria", on_delete=models.CASCADE)
    Empresa = models.ForeignKey(
        "Empresa", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.IntegerField(default=0)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    Imagen = models.ImageField(default= 'images/pan.png')
    def disponible(self):
        return self.Cantidad > 0


class Categoria(models.Model):
    Nombre = models.CharField(max_length=20)

    
class Empresa(models.Model):
    Nombre = models.CharField(max_length=20)

class Usuario(models.Model):
    Empresa = models.ForeignKey(
        "Empresa", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Correo = models.EmailField()
    Password = models.CharField(max_length=20)

class Venta(models.Model):
    Cliente = models.ForeignKey(
    "Cliente", on_delete=models.CASCADE)
    Producto = models.ForeignKey(
    "Producto", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.IntegerField()
    Precio = models.FloatField()
    Fecha = models.DateTimeField(auto_now_add=True)


class Cliente(models.Model):
    id= models.CharField(primary_key=True, max_length=20)
    Nombre = models.CharField(max_length=20)