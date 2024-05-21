from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    nombre = models.CharField(max_length=150, null = False)
    email = models.CharField(max_length=150, null = False)
    telefono = models.CharField(max_length = 15, null=True)
    
    def __str__(self) -> str:
        return str(self.nombre)