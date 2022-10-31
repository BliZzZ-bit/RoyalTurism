from django.urls import path
from .views import Home,crearDepartamento,listar_dep,editar_dep, eliminar_dep

urlpatterns = [
    path('',Home, name = 'index'),
    path('crear_departamento/',crearDepartamento, name='crear_departamento'),
    path('listar_deps/',listar_dep, name = 'listar_departamento'),
    path('editar_deps/<int:id>',editar_dep, name = 'editar_departamento'),
    path('eliminar_deps/<int:id>',eliminar_dep, name = 'eliminar_departamento')
    


]
