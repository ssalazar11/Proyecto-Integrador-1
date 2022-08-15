from inventario.models import usuario

def verificarUsuario(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = usuario.objects.filter(usuario=criterio).exists()
    return query

def verificarCorreo(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = usuario.objects.filter(correo=criterio).exists()
    return query
