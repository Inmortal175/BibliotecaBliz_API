from django.db import models

from .nacionalidad_model import Nacionalidad

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombres = models.CharField(max_length=30, null=False, help_text="Nombres del autor, este campo es obligatorio")
    apellido_paterno = models.CharField(max_length=30, null=False, help_text="Apellido paterno del autor, este campo es obligatorio")
    apellido_materno = models.CharField(max_length=30, null=False, help_text="Apellido materno del autor, este campo es obligatorio")
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, null = False)
    
    def __str__(self) -> str:
        return str(self.nombres + ', ' + self.apellido_paterno + ' ' + self.apellido_materno)