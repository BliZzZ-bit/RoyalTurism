import re
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import DepartamentoForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.


def Home(request):
    return render(request,'index.html')

def crearDepartamento(request):
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('index')
    else:
        departamento_form = DepartamentoForm()
        
    return render(request, 'web/crear_departamento.html',{'departamento_form':departamento_form})
