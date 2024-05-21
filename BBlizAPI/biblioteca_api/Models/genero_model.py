from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=350, null=True)
    
    def __str__(self):
        return str(self.nombre)