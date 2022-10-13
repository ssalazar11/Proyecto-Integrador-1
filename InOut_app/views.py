from math import prod
from django.shortcuts import render, redirect, HttpResponse
from .models import Producto, Venta, Usuario, Gop
from django.http import JsonResponse
import datetime
from InOut_app import logic, models
from collections import OrderedDict
from django.urls import reverse
from .forms import productoForm, Deleteform, actualizarProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

login_check = False
tipo = "mes"


def filter_time(query):
    global tipo
    if tipo == 'mes':
        filtro = 13
        top = 13*30
        timef = '%m/%d/%y'
    elif tipo == 'año':
        filtro = 13*30
        top = 12
        timef = '%m/%d/%y'
    elif tipo == 'dia':
        filtro = 1
        top = 24
        timef = "%m/%d/%H:%M"
    labels = []
    data = []
    cont = 0
    cantidad = 0
    for index, producto in enumerate(query, 0):
        labels.append([])
        data.append([])
        p = (list(producto))
        if len(p) > top:
            producto2 = p[len(p)-top:]
        else:
            producto2 = p
        print(producto2)
        for V in producto2:
            if cont == filtro:
                labels[index].append(V.Fecha.strftime(timef))
                data[index].append(cantidad)
                cantidad = 0
                cont = 0
            cantidad += (V.Cantidad)
            cont +=1
    return [labels, data]
    


def Registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellidos']
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        clave = request.POST['clave']

        if logic.verificarUsuario(usuario):
            messages.info(request,"Usuario ya se encuentra registrado, por favor selecciona otro ó inicia sesión")
        elif logic.verificarCorreo(correo):
            messages.info(request,"Correo ya se encuentra registrado, por favor selecciona otro ó inicia sesión")
        else:
            agregar = models.Usuario(nombre = nombre, apellido= apellido, usuario=usuario, correo=correo,clave=clave)
            agregar.save()
            return Home(request)

    return render(request, "registro.html")

def Ingreso(request):
    global login_check
    if login_check==True:
        return redirect('Productos')

    if request.method == "POST":
        
        usuario = request.POST['usuario']
        clave = request.POST['clave']

        try:
            informacion = models.Usuario.objects.get(usuario= usuario, clave=clave)
            login_check = True
            return redirect('Productos')

        except models.Usuario.DoesNotExist as e:
            messages.info(request, "Correo y/o contraseña incorrectos")

    return render(request, "Ingreso.html")


def Home(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    productos =  Producto.objects
    
    print(productos)
    return render(request, "Home.html", {"productos":productos})


def Usuario(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    return render(request, "Usuario.html")

def Productos(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    productos =  Producto.objects
    
    print(productos)
    return render(request, "Productos.html", {"productos":productos})

def graficas(request):
    #global login_check
    #if login_check==False:
        #return redirect('Welcome')
    labels = []
    data = []
    query = []
    names = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))
    
    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])
    
    
    for producto in Productos:
        (query.append(Venta.objects.filter(Producto_id = producto).order_by('Fecha')))

    filtrado = filter_time(query)
    labels = filtrado[0]
    data = filtrado[1]
    """
    for index, producto in enumerate(query, 0):
        labels.append([])
        data.append([])
        for V in producto:
            labels[index].append(V.Fecha.strftime('%m/%d/%y'))
            data[index].append(V.Cantidad)
    """
    return render(request, 'Graficas.html', {'labels': labels, 'data': data, 'names': names, 'n': len(names), 'number':list(range(0, len(names)))})

def Tendencias(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    return render(request, "Tendencias.html")


def Opciones(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    return render(request, "Opciones.html")

def Main(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
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
    global login_check
    if login_check==False:
        return redirect('Welcome')
    form=productoForm()
    context={'form':form}
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Productos')
    return render(request, 'agregar.html', context)


def EliminarItem(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('borrar', kwargs={"nombre": nombre}))
    return render(request, 'borrar2.html', context)


def modificar(request):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('actualizar', kwargs={"nombre": nombre}))
    return render(request, 'modificar.html', context)


def actualizar(request, nombre):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    try:
        productoactualizar = Producto.objects.get(Nombre=nombre)
    except:
        return redirect('modificar')
    if request.method == "POST":
        nombre = request.POST["producto"]
        cantidad = request.POST["cantidad"]
        actualizarProducto(nombre,cantidad)
        return redirect('Productos')
    context={'item':productoactualizar}
    return render(request, 'actualizar.html', context)



def Gmod(request):
    #global login_check
    global tipo
    #if login_check==False:
     #   return redirect('Welcome')
    if request.method == "POST":
        tipo = request.POST["fecha"]
        try:
            Tipo_data = Gop.objects.get(id=1)
            Tipo_data.timestep=tipo
            Tipo_data.save(update_fields =['timestep'])
        except:
            data = Gop(id=1, timestep=tipo)
            data.save()
        return redirect('Graficas')
    return render(request, 'Gmod.html')


def eliminacionProducto(request, nombre):
    global login_check
    if login_check==False:
        return redirect('Welcome')
    try:
        productoBorrar=Producto.objects.get(Nombre=nombre)
    except:
        return redirect('eliminar')
    if request.method == "POST":
        productoBorrar.delete()
        return redirect('Productos')
    context={'item':productoBorrar}
    return render(request, 'borrar.html', context)


def logOut_request(request):
    global login_check
    login_check = False
    return redirect("Welcome")

