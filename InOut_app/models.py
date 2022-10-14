from django.db import models

# Create your models here.

class Producto(models.Model):
    #Categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE) 
    #Empresa = models.ForeignKey( "Empresa", on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    Cantidad = models.IntegerField(default=0)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    Imagen = models.ImageField(default= 'pan.png')
    def disponible(self):
        return self.Cantidad > 0
    
    def __str__(self) -> str:
        return ("Nombre:%s, cantidad: %d, Precio: %d" % (self.Nombre, self.Cantidad, self.Precio))

class Venta(models.Model):
    Producto = models.ForeignKey(
    "Producto", on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Precio = models.FloatField()
    Fecha = models.DateTimeField()
    def __str__(self) -> str:
        return ("Nombre:%s, cantidad: %d, fecha: %s" % (self.Producto.Nombre, self.Cantidad, self.Fecha))
    #Cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)


class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=120)
    usuario = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)


class Gop(models.Model):
    timestep = models.CharField(max_length=60)
    Fecha = models.DateTimeField()
    mes = models.CharField(max_length=60)


"""
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




class Cliente(models.Model):
    id= models.CharField(primary_key=True, max_length=20)
    Nombre = models.CharField(max_length=20)
"""