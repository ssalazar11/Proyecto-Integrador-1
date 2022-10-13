from django.contrib import admin
from InOut_app.models import Producto, Venta, Usuario

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Usuario)