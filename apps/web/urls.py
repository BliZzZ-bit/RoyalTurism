from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name = 'index'),
    path('crear_departamento/',views.crearDepartamento, name='crear_departamento'),
    path('registro/', views.CrearUsuario, name="registro")
]
