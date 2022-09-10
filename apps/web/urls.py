from django.urls import path
from .views import crearDepartamento

urlpatterns = [
    path('crear_departamento/',crearDepartamento, name='crear_departamento')
]
