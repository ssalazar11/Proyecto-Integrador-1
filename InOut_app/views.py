from django.shortcuts import render, redirect, HttpResponse
from .models import Producto, Venta
from django.http import JsonResponse
import datetime
from collections import OrderedDict
from django.urls import reverse
from .forms import productoForm, Deleteform


def Registro(request):

    return render(request, "Registro.html")


def Ingreso(request):

    return render(request, "Ingreso.html")


def Home(request):
    productos =  Producto.objects
    
    print(productos)
    return render(request, "Home.html", {"productos":productos})


def Usuario(request):
    return render(request, "Usuario.html")

def Productos(request):
    productos =  Producto.objects
    
    print(productos)
    return render(request, "Productos.html", {"productos":productos})

def graficas(request):

    labels = []
    data = []
    query = []
    names = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])
    
    print(names)
    
    for producto in Productos:
        (query.append(Venta.objects.filter(Producto_id = producto).order_by('Fecha')))

   
    for index, producto in enumerate(query, 0):
        labels.append([])
        data.append([])
        for V in producto:
            labels[index].append(V.Fecha.strftime('%m/%d/%y'))
            data[index].append(V.Cantidad)
    print(names)
    return render(request, 'Graficas.html', {'labels': labels, 'data': data, 'names': names, 'n': len(names), 'number':list(range(0, len(names)))})

def Tendencias(request):

    return render(request, "Tendencias.html")


def Opciones(request):

    return render(request, "Opciones.html")

def Main(request):

    return render(request, "Main.html")


def Welcome(request):

    return render(request, "Welcome.html")

def get_data(request):
    data = {"sales":100,
            "customers":10,
    }
    return JsonResponse(data)

def test(request):
    labels = []
    data = []
    query = []
    names = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])
    
    print(names)
    
    for producto in Productos:
        (query.append(Venta.objects.filter(Producto_id = producto).order_by('Fecha')))

   
    for index, producto in enumerate(query, 0):
        labels.append([])
        data.append([])
        for V in producto:
            labels[index].append(V.Fecha.strftime('%m/%d/%y'))
            data[index].append(V.Cantidad)
    print(names)
    return render(request, 'test.html', {'labels': labels, 'data': data, 'names': names, 'n': len(names), 'number':list(range(0, len(names)))})




def registroProducto(request):
    form=productoForm()
    context={'form':form}
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Productos')
    return render(request, 'agregar.html', context)


def EliminarItem(request):
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('borrar', kwargs={"nombre": nombre}))
    return render(request, 'borrar2.html', context)


def eliminacionProducto(request, nombre):
    try:
        productoBorrar=Producto.objects.get(Nombre=nombre)
    except:
        return redirect('eliminar')
    if request.method == "POST":
        productoBorrar.delete()
        return redirect('Productos')
    context={'item':productoBorrar}
    return render(request, 'borrar.html', context)

