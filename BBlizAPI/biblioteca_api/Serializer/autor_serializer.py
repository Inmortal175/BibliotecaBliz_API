from rest_framework.serializers import ModelSerializer
from ..Models.autor_model import Autor
from rest_framework import serializers

class AutorModelSerializer(ModelSerializer):
    nacionalidad = serializers.SerializerMethodField()
    class Meta:
        model = Autor
        fields = ["id_autor", "nombres", "apellido_paterno", "apellido_materno", "nacionalidad"]

    def get_nacionalidad(self, obj):
        return obj.id_nacionalidad.gentilicio