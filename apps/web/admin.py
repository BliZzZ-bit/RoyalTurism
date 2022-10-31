from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento

class DepartamentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','estado','fecha_creacion']
    resource_class = DepartamentoResource


admin.site.register(Departamento,DepartamentoAdmin)