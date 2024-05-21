from django.db import models

from .usuario_model import UsuarioBiblioteca
from bibliotecario.models import Bibliotecario
from .devolucion_model import Devolucion

class Prestamo (models.Model):
    id_prestamo      = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    fecha_prestamo   = models.DateField(null = False, blank = False)
    fecha_caducidad  = models.DateField(null = False, blank = False)
    
    #foreimg keys
    id_usuario       = models.ForeignKey(UsuarioBiblioteca, on_delete=models.CASCADE, null= False, blank=False)
    id_bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE, null= False, blank=False)
    id_devolucion    = models.ForeignKey(Devolucion, on_delete=models.CASCADE, null= True, blank=True)
    
    def __str__(self) -> str:
        return str(str(self.fecha_prestamo) + " / " + self.id_usuario.nombres)