from django.db import models

class Devolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    fecha_devolucion = models.DateField(null=False)
    
    def __str__(self):
        return str(self.id_devolucion)