from django.urls import path
from . import views

urlpatterns=[
    path('', views.productoPag, name="producto"),
    path('opciones', views.opciones, name="opciones"),
    path('usuario', views.usuario, name="usuario"),
    path('agregar', views.registroProducto, name="agregar"),
    path('eliminar', views.eliminacionProducto, name="borrar"),
    path('admin', views.adminUsuario, name="adminUsuario"),
]