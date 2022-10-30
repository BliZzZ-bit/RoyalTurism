from pyexpat import model
from tabnanny import verbose
from django.db import models
from django import forms

# Create your models here.
class Departamento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200,blank = False, null = False)
    numero = models.IntegerField()
    direccion = models.CharField(max_length = 200,blank = False, null = False)
    num_habitaciones = models.IntegerField()
    num_baños = models.IntegerField()
    descripcion = models.TextField(blank = False, null = False)
    valor = models.IntegerField()
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamentos'
        verbose_name_plural = 'Departamentos'

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    rut_usuario = models.CharField(max_length = 200,blank = False, null = False)
    nombre = models.CharField(max_length = 200,blank = False, null = False)
    a_paterno = models.CharField(max_length = 200,blank = False, null = False)
    a_materno = models.CharField(max_length = 200,blank = False, null = False)
    email = models.EmailField(max_length = 254,blank = False, null = False)
    num_contacto = models.IntegerField()
    tipo_de_usuario = models.CharField(max_length = 200,blank = False, null = False)
    password = forms.CharField(max_length=100)

    def __str__(self):
        return self.rut_usuario

    class Meta:
        
        ordering = ['rut_usuario']
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
