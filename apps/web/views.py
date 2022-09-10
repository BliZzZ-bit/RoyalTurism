from django.shortcuts import render, redirect
from .forms import DepartamentoForm




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