from ..Models.usuario_model import UsuarioBiblioteca
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class RepoprteUsuarioModelSerializer(ModelSerializer):
    cant_prestamos = serializers.IntegerField()
    agregado_por = serializers.CharField()

    class Meta:
        model = UsuarioBiblioteca
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'es_activo', 'cant_prestamos', 'fecha_creacion', 'agregado_por']