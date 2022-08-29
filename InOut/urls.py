"""InOut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InOut_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registro/', views.Registro, name="Registro"),
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('Home/',   views.Home, name="Home"),
    path('Usuario/', views.Usuario, name="Usuario"),
    path('Productos/', views.Productos, name="Productos"),
    path('Graficas/', views.graficas, name="Graficas"),
    path('Tendencias/', views.Tendencias, name="Tendencias"),
    path('Opciones/', views.Opciones, name="Opciones")
]
