# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from Models.bibliotecario_model import Bibliotecario as user
# # Register your models here.

# @admin.register(user)
# class Bibliotecario(UserAdmin):
#     fieldsets = 'all'

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Bibliotecario
from .forms import BibliotecarioCreationForm, BibliotecarioChangeForm

class BibliotecarioAdmin(UserAdmin):
    add_form = BibliotecarioCreationForm
    form = BibliotecarioChangeForm
    model = Bibliotecario
    list_display = ('usuario', 'email', 'nombres', 'apellido_paterno', 'apellido_materno', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('usuario', 'email', 'password')}),
        ('Personal info', {'fields': ('nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'email', 'password1', 'password2', 'nombres', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('usuario', 'email')
    ordering = ('usuario',)

admin.site.register(Bibliotecario, BibliotecarioAdmin)