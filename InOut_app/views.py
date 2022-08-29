from django.shortcuts import render, HttpResponse

# Create your views here.

def Registro(request):

    return HttpResponse("Registro")


def Ingreso(request):

    return HttpResponse("Ingreso")


def Home(request):

    return HttpResponse("Home")


def Usuario(request):

    return HttpResponse("Usuario")

def Productos(request):

    return HttpResponse("Producto")

def graficas(request):

    return HttpResponse("Graficas")

def Tendencias(request):

    return HttpResponse("Tendencias")


def Opciones(request):

    return HttpResponse("Opciones")


