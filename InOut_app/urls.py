from django.urls import path
from InOut_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Welcome, name="Welcome"),
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
    path('Logout/', views.logOut_request, name="Logout"),
    path('api/get_data/', views.get_data, name='api-data'),
    path('test/', views.test, name='test'),
    path('agregar/', views.registroProducto, name="agregar"),
    path('eliminar/', views.EliminarItem, name="eliminar"),
    path('eliminar/<str:nombre>', views.eliminacionProducto, name="borrar"),
    path('actualizar/<str:nombre>', views.actualizar, name="actualizar"),
    path('actualizar/', views.modificar, name="modificar"),
    path('Gmod/', views.Gmod, name="Gmod"),
    path('Reset/', views.Reset, name="Reset"),
    path('Tmood/', views.Tmood, name="Tmood"),
    path('pind/', views.pind, name="pind"),
    path('pind/<str:id_obj>', views.pind, name="pind"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)