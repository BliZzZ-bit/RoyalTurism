from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import DepartamentoForm
from .models import Departamento

# Create your views here.


def Home(request):
    return render(request,'index.html')

def crearDepartamento(request):
    if request.method == 'POST':
        print(request.POST)
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('index')
    else:
        departamento_form = DepartamentoForm()
    return render(request, 'web/crear_departamento.html',{'departamento_form':departamento_form})

def listar_dep(request):
    deps = Departamento.objects.all()
    return render(request, 'web/listardeps.html', {'deps':deps})

def editar_dep(request,id):
    departamento_form = None
    error = None
    try:
        deps = Departamento.objects.get(id = id)
        if request.method == 'GET':
            departamento_form = DepartamentoForm(instance = deps)
        else:
            departamento_form = DepartamentoForm(request.POST, instance = deps)
            if departamento_form.is_valid():
                departamento_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'web/crear_departamento.html',{'departamento_form':departamento_form,'error':error})



'''
def registrar(request):
    return render(request, 'registro.html', {
            'form': UserCreationForm
    })
'''