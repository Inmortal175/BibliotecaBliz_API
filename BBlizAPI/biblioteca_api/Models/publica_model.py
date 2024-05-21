from django.db import models
from .libro_model import Libro
from .editorial_model import Editorial
class Publica (models.Model):
    id_publica   = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    
    #foreingkey
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null= False)
    id_libro     = models.ForeignKey(Libro,on_delete=models.CASCADE, null= False)