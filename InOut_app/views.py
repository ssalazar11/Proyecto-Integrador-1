from math import prod
from django.shortcuts import render, redirect, HttpResponse
from .models import Producto, Venta, Usuario, Gop
from django.http import JsonResponse
import datetime
from InOut_app import logic, models
from collections import OrderedDict
from django.urls import reverse
from .forms import productoForm, Deleteform, actualizarProducto, VentaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#tipo = "mes"
#fecha = 'nulo'
#mes = 6
meses={
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',

}


def filter_time(query):
    opciones = ((Gop.objects.filter(id = 1)))
    print(opciones[0].Fecha)
    tipo = opciones[0].timestep
    fecha = opciones[0].Fecha
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
        print(fecha.strftime('%Y'))
        if int(fecha.strftime('%Y')) < 2000:
            if len(p) > top:
                producto2 = p[len(p)-top:]
            else:
                producto2 = p
        else: 
            i = 0
            print(len(p))
            try:
                i = 0
                while i < (len(p)):
                    if p[i].Fecha >= fecha:
                        break;
                    i+=1
                producto2 = p[i:i+top]
                print('Logrado')
            except:
                if len(p) > top:
                    producto2 = p[len(p)-top:]
                else:
                    producto2 = p
                print('Mori')
        for V in producto2:
            if cont == filtro:
                labels[index].append(V.Fecha.strftime(timef))
                data[index].append(cantidad)
                cantidad = 0
                cont = 0
            cantidad += (V.Cantidad)
            cont +=1
    return [labels, data]
    

def Reset(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    Tipo_data = Gop.objects.get(id=1)
    Tipo_data.timestep='mes'
    Tipo_data.Fecha=datetime.datetime(1990,1,1)
    Tipo_data.save(update_fields =['timestep','Fecha'])
    return graficas(request)


def Registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellidos']
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        clave = request.POST['clave']

        user = User.objects.create_user(usuario, correo, clave)
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        return render(request, "welcome.html")
    return render(request, "registro.html")

def Ingreso(request):
    if  request.user.is_authenticated:
        return redirect('Productos')
    if request.method == "POST":
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        user = authenticate(request, username = usuario, password = clave)
        if user is not None:
            login(request, user)
            return redirect('Productos')
        else:
            messages.info(request, "Correo y/o contraseña incorrectos")

    return render(request, "Ingreso.html")




def Home(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    productos =  Producto.objects
    return render(request, "Home.html", {"productos":productos})


def usuario(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    nombreUsuario=request.user
    datos=Usuario.objects.filter(usuario=nombreUsuario)
    return render(request, "Usuario.html", {'datos':datos})

def Productos(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    productos =  Producto.objects.filter(Usuario_id=request.user)
    return render(request, "Productos.html", {"productos":productos})

def graficas(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
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
    if not request.user.is_authenticated:
        return redirect('welcome')
    opciones = ((Gop.objects.filter(id = 1)))
    mes = int(opciones[0].mes)
    horas2 = tendenciashoras2(mes)
    meses = tendeciames(mes)
    horas = tendenciashoras()
    compara = mejor()
    return render(request, "Tendencias.html", {'horas2': horas2, 'meses':meses, 'horas':horas, 'compara':compara })


def tendenciashoras2(mes):
    query = []
    names = []
    productos = []
    mañana = ['06','07','08','09','10']
    medio = ['11','12','13','14']
    tarde=['15','16','17','18']
    ret = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])

    for producto in Productos:
        (query.append(list(Venta.objects.filter(Producto_id = producto).order_by('Fecha'))))
    print("Holaaaaaaa")
    print(len(query))
    for producto in query:
        ma = 0
        me = 0
        t = 0
        cont1 = 0
        cont2 = 0
        cont3 = 0
        for venta in producto:
            
            if venta.Fecha.strftime('%H') in mañana and int(venta.Fecha.strftime('%m')) == mes:
                cont1 += 1
                ma += venta.Cantidad
            elif venta.Fecha.strftime('%H') in medio and int(venta.Fecha.strftime('%m')) == mes:
                cont2 += 1
                me += venta.Cantidad
            elif venta.Fecha.strftime('%H') in tarde and int(venta.Fecha.strftime('%m')) == mes:
                cont3 += 1
                t += venta.Cantidad
        productos.append([ma/(cont1/5),me/(cont2/4),t/(cont3/4)])
    
    print(productos)
    print(names)
    ma = []
    me = []
    t = []
    for i in productos:
        ma.append(i[0])
        me.append(i[1])
        t.append(i[2])
    ret.append(("El producto mas vendido en las mañanas del mes de %s fue el %s, con un promedio de %d ventas" % (meses[mes], names[ma.index(max(ma))],max(ma))))
    ret.append(("El producto mas vendido al medio dia en el mes de %s fue el %s, con un promedio de %d ventas"% (meses[mes], names[me.index(max(me))],max(me))))
    ret.append(("El producto mas vendido en las tardes del mes de %s fue el %s, con un promedio de %d ventas" % (meses[mes], names[t.index(max(t))],max(t))))
    return(ret)
        


def tendenciashoras():
    query = []
    names = []
    productos = []
    mañana = ['06','07','08','09','10']
    medio = ['11','12','13','14']
    tarde=['15','16','17','18']
    ret = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])

    for producto in Productos:
        (query.append(list(Venta.objects.filter(Producto_id = producto).order_by('Fecha'))))
    for producto in query:
        ma = 0
        me = 0
        t = 0
        cont1 = 0
        cont2 = 0
        cont3 = 0
        mes = int(producto[-1].Fecha.strftime('%m'))
        print(mes)
        for venta in producto:
            if venta.Fecha.strftime('%H') in mañana and int(venta.Fecha.strftime('%m')) == mes:
                ma += venta.Cantidad
                cont1 += 1
            elif venta.Fecha.strftime('%H') in medio and int(venta.Fecha.strftime('%m')) == mes:
                me += venta.Cantidad
                cont2 += 2
            elif venta.Fecha.strftime('%H') in tarde and int(venta.Fecha.strftime('%m')) == mes:
                t += venta.Cantidad
                cont3 += 3
        productos.append([ma/(cont1/5),me/(cont2/4),t/(cont3/4)])

    print(productos)
    print(names)
    ma = []
    me = []
    t = []
    for i in productos:
        ma.append(i[0])
        me.append(i[1])
        t.append(i[2])
    ret.append(("El producto mas vendido en las mañanas del mes de %s fue el %s, con un promedio de %d ventas" % (meses[mes], names[ma.index(max(ma))],max(ma))))
    ret.append(("El producto mas vendido al medio dia en el mes de %s fue el %s, con un promedio de %d ventas"% (meses[mes], names[me.index(max(me))],max(me))))
    ret.append(("El producto mas vendido en las tardes del mes de %s fue el %s, con un promedio de %d ventas" % (meses[mes], names[t.index(max(t))],max(t))))
    return(ret)


def tendeciames(mes):
    query = []
    names = []
    productos = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])

    for producto in Productos:
        (query.append(list(Venta.objects.filter(Producto_id = producto).order_by('Fecha'))))

    for producto in query:
        cont = 0
        cont2 = 0
        for venta in producto:
            if int(venta.Fecha.strftime('%m')) == mes:
                cont2 += 1
                cont += venta.Cantidad
        print(cont2)
        productos.append([cont/(cont2/13)])
    return("El producto mas vendido en el mes %s fue el %s con un promedio de %d unidades vendidas al dia" %(meses[mes],names[productos.index(max(productos))], max(productos)[0]))


def mejor():
    query = []
    names = []
    actual = []
    pasado = []
    productos = []
    relacion = []
    ret = []
    Productos = ((Venta.objects.values_list('Producto_id', flat=True).distinct()))

    for id_p in Productos:
        names.append((Producto.objects.filter(id=id_p)).values()[0]['Nombre'])

    for producto in Productos:
        (query.append(list(Venta.objects.filter(Producto_id = producto).order_by('Fecha'))))

    for producto in query:
        diaf = int(producto[-1].Fecha.strftime('%d'))
        if diaf > 27:
            diaf = 27
        mesf = int(producto[-1].Fecha.strftime('%m'))
        cont = 0
        cont2 = 0
        for venta in producto:
            if int(venta.Fecha.strftime('%m')) == mesf and int(venta.Fecha.strftime('%d')) < diaf:
                cont += venta.Cantidad
            elif int(venta.Fecha.strftime('%m')) == mesf-1 and int(venta.Fecha.strftime('%m')) < diaf-1:
                cont2 += venta.Cantidad
        productos.append([cont, cont2])
    print(productos)
    for i in range(len(productos)):
        relacion.append(((productos[i][1]-productos[i][0])/abs(productos[i][0]))*100)
    print(relacion)
    for i in  range (len(relacion)):
        if relacion[i] > 0:
            ret.append("El producto %s ha tenido una mejora del %.2f %s  con respecto al mes anterior" % (names[i], relacion[i], '%'))
        else:
            ret.append("El producto %s ha bajado su rendimiento un %.2f %s  con respecto al mes anterior" % (names[i], relacion[i], '%'))
    return(ret)


def Opciones(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "Opciones.html")

def Main(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "Main.html")


def Welcome(request):

    return render(request, "Welcome.html")


def pind(request, id_obj):
    if not request.user.is_authenticated:
        return redirect('welcome')
    query = []
    labels = []
    data = []
    p = Producto.objects.filter(id=id_obj)
    name = p[0].Nombre
    query.append(Venta.objects.filter(Producto_id = id_obj).order_by('Fecha'))
    filtrado = filter_time(query)
    labels = filtrado[0]    
    data = filtrado[1]
    return render(request, "pind.html", {'labels': labels[0], 'data': data[0], 'producto': p[0]})


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
    
    
    for producto in Productos:
        (query.append(Venta.objects.filter(Producto_id = producto).order_by('Fecha')))

   
    for index, producto in enumerate(query, 0):
        labels.append([])
        data.append([])
        for V in producto:
            labels[index].append(V.Fecha.strftime('%m/%d/%y'))
            data[index].append(V.Cantidad)
    return render(request, 'test.html', {'labels': labels, 'data': data, 'names': names, 'n': len(names), 'number':list(range(0, len(names)))})




def registroProducto(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=productoForm()
    context={'form':form}
    if request.method == 'POST':
        form=productoForm(request.POST, request.FILES)
        if form.is_valid():            
            product = form.save(commit=False)
            product.Usuario_id=request.user.id
            product.save()
            return redirect('Productos')
    return render(request, 'agregar.html', context)


def AgregarVenta(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=VentaForm()
    context={'form':form}
    if request.method == 'POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Productos')
    return render(request, 'agregar.html', context)


def EliminarItem(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('borrar', kwargs={"nombre": nombre}))
    return render(request, 'borrar2.html', context)


def modificar(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('actualizar', kwargs={"nombre": nombre}))
    return render(request, 'modificar.html', context)


def actualizar(request, nombre):
    if not request.user.is_authenticated:
        return redirect('welcome')
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
    global tipo
    global fecha
    if not request.user.is_authenticated:
        return redirect('welcome')
    if request.method == "POST":
        tipo = request.POST["fecha"]
        fecha = request.POST["fechaini"]
        try:
            Tipo_data = Gop.objects.get(id=1)
            Tipo_data.timestep=tipo
            Tipo_data.Fecha=fecha
            Tipo_data.save(update_fields =['timestep','Fecha'])
        except:
            data = Gop(id=1, timestep=tipo)
            data.save()
        return redirect('Graficas')
    return render(request, 'Gmod.html')


def Tmood(request):
    global tipo
    global fecha
    if not request.user.is_authenticated:
        return redirect('welcome')
    if request.method == "POST":
        mes = request.POST["fecha"]
        try:
            Tipo_data = Gop.objects.get(id=1)
            Tipo_data.mes=mes
            Tipo_data.save(update_fields =['mes'])
        except:
            data = Gop(id=1, timestep=tipo)
            data.save()
        return redirect('Tendencias')
    return render(request, 'Tmood.html')


def eliminacionProducto(request, nombre):
    if not request.user.is_authenticated:
        return redirect('welcome')
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
    logout(request)
    return redirect("Welcome")

