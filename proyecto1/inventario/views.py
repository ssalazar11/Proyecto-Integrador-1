from django.shortcuts import render, redirect
from .models import *
from .forms import productoForm
# Create your views here.

def registroProducto(request):
    form=productoForm()
    context={'form':form}
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminUsuario')
    return render(request, 'agregar.html', context)

def eliminacionProducto(request, nombre):
    productoBorrar=producto.objects.get(nombreProducto=nombre)
    if request.method == "POST":
        productoBorrar.delete()
        return redirect('adminUsuario')
    context={'item':productoBorrar}
    return render(request, 'borrar.html', context)


def adminUsuario(request):
    productos=producto.objects.all()
    context={'producto':productos}
    return render(request, "adminUsuario.html",context)

def productoPag(request):
    return render(request, "producto.html")

def opciones(request):
    return render(request, "opciones.html")

def usuario(request):
    return render(request, "usuario.html")