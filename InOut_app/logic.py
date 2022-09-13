from .models import Usuario

def verificarUsuario(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = Usuario.objects.filter(usuario=criterio).exists()
    return query

def verificarCorreo(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = Usuario.objects.filter(correo=criterio).exists()
    return query
