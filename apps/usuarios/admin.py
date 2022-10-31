from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['username','nombre','u_activo','email']
    resource_class = UsuarioResource
# Register your models here.
admin.site.register(Usuario,UsuarioAdmin)