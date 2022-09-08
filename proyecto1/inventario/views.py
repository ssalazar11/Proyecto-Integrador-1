from django.shortcuts import render
from inventario import models
# Create your views here.

def registroProducto(request):
    if request.method == 'POST':
        nombreProducto=request.POST['nombreProducto']
        tipoProducto=request.POST['tipoProducto']
        cantidadProducto=request.POST['cantidadProducto']
        agregar=models.producto(nombreProducto=nombreProducto, tipoProducto=tipoProducto, cantidadProducto=cantidadProducto)
        agregar.save()

def eliminacionProducto(request, nombre):
    if request.method == 'POST':
        producto=producto.objects.get(nombreProducto=nombre)
        producto.delete()
        

def producto(request):
    return render(request, "producto.html")

def opciones(request):
    return render(request, "opciones.html")

def usuario(request):
    return render(request, "usuario.html")