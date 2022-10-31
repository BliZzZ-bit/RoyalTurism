from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import Formulariologin

# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = Formulariologin
    success_url = reverse_lazy('')