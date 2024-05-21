from django.db import models

from bibliotecario.models import Bibliotecario
class UsuarioBiblioteca(models.Model):
    id_usuario = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombres = models.CharField(max_length= 30, null=False)
    apellido_paterno = models.CharField(max_length= 30, null=False)
    apellido_materno = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=150, null=False)
    es_activo = models.BooleanField('usuario activo', default=True)
    id_bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE, null=False)
    
    def __str__(self) -> str:
        return str(self.nombres + ', ' + self.apellido_paterno + ' ' + self.apellido_materno)