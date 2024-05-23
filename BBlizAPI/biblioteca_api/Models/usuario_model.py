from django.db import models
from datetime import datetime
from bibliotecario.models import Bibliotecario
class UsuarioBiblioteca(models.Model):
    id_usuario = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombres = models.CharField(max_length= 30, null=False)
    apellido_paterno = models.CharField(max_length= 30, null=False)
    apellido_materno = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=150, null=False)
    es_activo = models.BooleanField('usuario activo', default=True)
    fecha_creacion = models.DateTimeField(auto_created=True, auto_now_add=True, blank=False, null=False)
    id_bibliotecario = models.ForeignKey(Bibliotecario,  null=False, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.nombres + ', ' + self.apellido_paterno + ' ' + self.apellido_materno)