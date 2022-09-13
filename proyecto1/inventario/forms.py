from django.forms import ModelForm
from .models import producto
from inventario.models import producto as prd
import sqlite3

def actualizarProducto(producto,cantidad):
    target = prd.objects.get(nombreProducto=producto)
    target.cantidadProducto = cantidad
    target.save(update_fields =['cantidadProducto'])

class productoForm(ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

