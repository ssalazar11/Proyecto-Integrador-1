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

def eliminacionProducto(request):
    if request.method == 'POST':
        producto=producto.objects.get(id=pk)
        producto.delete()
        return redirect('adminUsuario')
    #context={'item':producto}
    return render(request, 'borrar.html')


def adminUsuario(request):
    productos=producto.objects.all()
    return render(request, "adminUsuario.html", {'producto':productos})

def productoPag(request):
    return render(request, "producto.html")

def opciones(request):
    return render(request, "opciones.html")

def usuario(request):
    return render(request, "usuario.html")