from rest_framework.serializers import ModelSerializer
from ..Models.publica_model import Publica
from rest_framework import serializers

class PublicaModelSerializer(ModelSerializer):
    
    editorial = serializers.SerializerMethodField()
    libro = serializers.SerializerMethodField()
    
    class Meta:
        model = Publica
        fields = '__all__'
        
    # def get_editorial(self, obj):
    #     return obj.id_editorial.nombre
    
    # def get_libro(self, obj):
    #     return obj.id_libro.titulo