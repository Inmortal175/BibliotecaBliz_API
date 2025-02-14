from django.db import models

from .libro_model import Libro
from .prestamo_model import Prestamo

class DetallePrestamo(models.Model):
    id_detalle_prestamo = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    
    #FK
    id_prestamo = models.ForeignKey( Prestamo, on_delete=models.CASCADE, null = False, blank=False)
    id_libro    = models.ForeignKey( Libro, on_delete=models.CASCADE, null = False, blank=False)