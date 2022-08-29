from django.urls import path
from InOut_app import views

urlpatterns = [
    path('Registro/', views.Registro, name="Registro"),
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('Home/',   views.Home, name="Home"),
    path('Usuario/', views.Usuario, name="Usuarios"),
    path('Productos/', views.Productos, name="Productos"),
    path('Graficas/', views.graficas, name="Graficas"),
    path('Tendencias/', views.Tendencias, name="Tendencias"),
    path('Opciones/', views.Opciones, name="Opciones"),
    path('Main/', views.Main, name="Main"),
    path('Welcome/', views.Welcome, name="Welcome"),
    path('Logout/', views.Welcome, name="Logout")
]