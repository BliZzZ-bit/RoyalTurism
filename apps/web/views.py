from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import DepartamentoForm, UsuarioForm

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

def CrearUsuario(request):
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('index')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'registro.html',{'usuario_form':usuario_form})