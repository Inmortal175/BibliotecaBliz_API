from django.db import models

class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True, auto_created=True, unique=True, db_index=True)
    pais = models.CharField(max_length = 50, null = False)
    gentilicio = models.CharField(max_length = 50, null = False, help_text="Ejemplo: peruano (a)")
    
    def __str__(self) -> str:
        return str(self.gentilicio)