from django.forms import ModelForm
from .models import Producto, Venta
from django import forms

class Deleteform(forms.Form):
    Nombre = forms.CharField(required=True, max_length=50)


class productoForm(ModelForm):
    class Meta:
        model = Producto
        fields = {'Nombre','Cantidad','Precio','Imagen'}


class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = {'Producto','Cantidad','Fecha','Precio', 'id'}

def actualizarProducto(producto,cantidad):
    target = Producto.objects.get(Nombre=producto)
    target.Cantidad = cantidad
    target.save(update_fields =['Cantidad'])