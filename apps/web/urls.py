from django.urls import path
from .views import crearDepartamento, Home

urlpatterns = [
    path('',Home, name = 'index'),
    path('crear_departamento/',crearDepartamento, name='crear_departamento')
]
