from django.forms import ModelForm
from .models import Producto
from django import forms

class Deleteform(forms.Form):
    Nombre = forms.CharField(required=True, max_length=50)


class productoForm(ModelForm):
    class Meta:
        model = Producto
        fields = {'Nombre','Cantidad','Precio'}


def actualizarProducto(producto,cantidad):
    target = Producto.objects.get(Nombre=producto)
    target.Cantidad = cantidad
    target.save(update_fields =['Cantidad'])