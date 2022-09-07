from django.urls import path
from . import views

urlpatterns=[
    path('', views.producto, name="producto"),
    path('opciones', views.opciones, name="opciones"),
    path('usuario', views.usuario, name="usuario"),
]