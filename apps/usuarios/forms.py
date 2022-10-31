from django.contrib.auth.forms import AuthenticationForm

class Formulariologin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(Formulariologin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'