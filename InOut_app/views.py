from django.shortcuts import render, HttpResponse

# Create your views here.

def Registro(request):

    return render(request, "Registro.html")


def Ingreso(request):

    return render(request, "Ingreso.html")


def Home(request):

    return render(request, "Home.html")


def Usuario(request):
    return render(request, "Usuario.html")

def Productos(request):

    return render(request, "Productos.html")

def graficas(request):

    return render(request, "Graficas.html")

def Tendencias(request):

    return render(request, "Tendencias.html")


def Opciones(request):

    return render(request, "Opciones.html")

def Main(request):

    return render(request, "Main.html")

