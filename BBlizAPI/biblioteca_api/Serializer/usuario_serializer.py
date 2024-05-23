from rest_framework.serializers import ModelSerializer
from ..Models.usuario_model import UsuarioBiblioteca

from rest_framework import serializers

class UsuarioModelSerializer(ModelSerializer):
    # bibliotecario = serializers.CharField(source='id_bibliotecario.get_full_name')
    bibliotecario = serializers.SerializerMethodField()
    # CharField(source='id_bibliotecario.nombres')
    class Meta:
        model = UsuarioBiblioteca
        fields = ['id_usuario', 'nombres', 'apellido_paterno', 'apellido_materno', 'telefono', 'email', 'es_activo', 'bibliotecario']
    
    def get_bibliotecario(self, obj):
        return f"{obj.id_bibliotecario.apellido_paterno} {obj.id_bibliotecario.apellido_materno}, {obj.id_bibliotecario.nombres}"
    
class UsuarioCreatedSerializer(ModelSerializer):
    class Meta:
        model = UsuarioBiblioteca
        fields = '__all__'