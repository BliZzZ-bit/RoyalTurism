from dataclasses import field, fields
from django import forms
from .models import Departamento, Usuario

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento 
        fields = ['nombre', 'numero', 'direccion', 'num_habitaciones', 'num_baños', 'descripcion', 'valor'
        ]
        

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['rut_usuario', 'nombre', 'a_paterno', 'a_materno', 'email', 'num_contacto', 'tipo_de_usuario', 'password'
        ]
