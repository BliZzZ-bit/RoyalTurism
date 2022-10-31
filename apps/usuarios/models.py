from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    pass
    def create_user(self,email,username,nombre,apellidos,password = None):
        if not email:
            raise ValueError('El usuario debe tener un email!')
        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email), 
            nombre = nombre,
            apellidos = apellidos
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombre,apellidos,password):
        usuario = self.create_user(
            email,
            username = username,
            nombre = nombre,
            apellidos = apellidos,
            password = password
            )
        usuario.u_admin = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length = 100)
    email = models.EmailField('Email',max_length = 100, unique = True)
    nombre = models.CharField('Nombres', max_length = 100, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length = 100, blank = True, null = True)
    u_activo = models.BooleanField(default = True)
    u_admin =models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellidos']

    def _str_(self):
        return f'{self.nombre},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.u_admin