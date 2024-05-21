# bibliotecario/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Bibliotecario

class BibliotecarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Bibliotecario
        fields = ('usuario', 'email', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono')

class BibliotecarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Bibliotecario
        fields = ('usuario', 'email', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'is_staff', 'is_active')
