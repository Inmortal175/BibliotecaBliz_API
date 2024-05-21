from django.db import models

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombre = models.CharField(max_length = 50, null = False)
    direccion = models.CharField(max_length = 150, null = False)
    email = models.CharField(max_length = 150, null = False)
    telefono = models.CharField(max_length = 15, null = True)
    
    def __str__(self) -> str:
        return str(self.nombre)