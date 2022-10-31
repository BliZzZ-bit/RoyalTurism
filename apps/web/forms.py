from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento 
        fields = ['nombre', 'numero', 'direccion', 'num_habitaciones', 'num_baños', 'descripcion', 'valor'
        ]
        
