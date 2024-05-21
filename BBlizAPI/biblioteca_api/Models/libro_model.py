from django.db import models

from .proveedor_model import Proveedor
from .autor_model import Autor
from .genero_model import Genero
from bibliotecario.models import Bibliotecario

class Libro(models.Model):
    id_libro         = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    titulo           = models.CharField(max_length=150, null=False)
    anio_publicacion = models.IntegerField(null=False)
    cantidad         = models.IntegerField(null= False)
    descripcion      = models.CharField(max_length=1500, null=True)
    
    #foreingkeys
    id_autor         = models.ForeignKey(Autor, on_delete=models.CASCADE, null= False)
    id_genero        = models.ForeignKey(Genero, on_delete=models.CASCADE, null= False)
    id_proveedor     = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null= False)
    id_bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE, null= False)
    
    def __str__(self) -> str:
        return str(self.titulo + " Genero: " + self.id_genero.nombre)