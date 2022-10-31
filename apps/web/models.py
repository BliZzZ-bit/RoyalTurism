
from email.policy import default
from django.db import models

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
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)

    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
