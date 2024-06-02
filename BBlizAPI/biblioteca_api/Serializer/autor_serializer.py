from rest_framework.serializers import ModelSerializer
from ..Models.autor_model import Autor
from ..Models.nacionalidad_model import Nacionalidad
from rest_framework import serializers

class AutorModelSerializer(ModelSerializer):
    nacionalidad = serializers.SerializerMethodField() #PrimaryKeyRelatedField(queryset=Nacionalidad.objects.all(), source='id_nacionalidad__gentilicio')

    def get_nacionalidad(self, obj):
        return obj.id_nacionalidad.gentilicio
    
    class Meta:
        model = Autor
        fields = ["id_autor", "nombres", "apellido_paterno", "apellido_materno", "nacionalidad"]

class AutorCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'





'''
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
'''