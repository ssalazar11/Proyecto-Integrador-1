from django.shortcuts import render

# Create your views here.

def producto(request):
    return render(request, "producto.html")

def opciones(request):
    return render(request, "opciones.html")

def usuario(request):
    return render(request, "usuario.html")