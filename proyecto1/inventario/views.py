from django.shortcuts import render
from inventario import models
from inventario import logic
from django.contrib import messages
from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
login_check = False
def Index(request):
    return render(request, "index.html")

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
            agregar = models.usuario(nombre = nombre, apellido= apellido, usuario=usuario, correo=correo,clave=clave)
            agregar.save()
            return Home(request)

    return render(request, "registro.html")

def Ingreso(request):
    global login_check
    if login_check:
        return render(request, 'Home.html')

    if request.method == "POST":
        
        usuario = request.POST['usuario']
        clave = request.POST['clave']

        try:
            informacion = models.usuario.objects.get(usuario= usuario, clave=clave)
            return render(request, "Home.html")

        except models.usuario.DoesNotExist as e:
            messages.info(request, "Correo y/o contraseña incorrectos")

    return render(request, "ingresar.html")

def Home(request):
    return render(request, "Home.html")

def logOut_request(request):
    global login_check
    login_check = False
    return render(request, "logout.html")
