from rest_framework.serializers import ModelSerializer
from ..Models.libro_model import Libro

# crear un campo personalizado de sializador
from rest_framework import serializers


class LibroModelSerializer(ModelSerializer):

    prestados = serializers.IntegerField(read_only=True)

    class Meta:
        model = Libro
        fields = ["id_libro", "titulo", "descripcion", "cantidad", "prestados"]
