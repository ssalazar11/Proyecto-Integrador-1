from django.urls import path
from InOut_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Welcome, name="Welcome"),
    path('Registro/', views.Registro, name="Registro"),
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('Home/',   views.Home, name="Home"),
    path('Usuario/', views.usuario, name="Usuarios"),
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
    path('agregarV/', views.AgregarVenta, name="agregarV"),
    path('eliminar/', views.EliminarItem, name="eliminar"),
    path('eliminar/<str:nombre>', views.eliminacionProducto, name="borrar"),
    path('actualizar/<str:nombre>', views.actualizar, name="actualizar"),
    path('actualizar/', views.modificar, name="modificar"),
    path('Gmod/', views.Gmod, name="Gmod"),
    path('Gmod2/', views.Gmod2, name="Gmod2"),
    path('Reset/', views.Reset, name="Reset"),
    path('Reset2/', views.Reset2, name="Reset2"),
    path('Reset3/', views.Reset3, name="Reset3"),
    path('Tmood/', views.Tmood, name="Tmood"),
    path('pind/', views.pind, name="pind"),
    path('Comparar/', views.Comparar, name="Comparar"),
    path('pind/<str:id_obj>', views.pind, name="pind"),
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)