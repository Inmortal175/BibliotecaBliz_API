from rest_framework.serializers import ModelSerializer
from ..Models.prestamo_model import Prestamo

from rest_framework import serializers

class PrestamoCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class PrestamoModelSerializer(ModelSerializer):
    usuario = serializers.SerializerMethodField()
    bibliotecario = serializers.SerializerMethodField()
    estado_devolucion = serializers.SerializerMethodField()
    
    def get_usuario(self, obj):
        return f"{obj.id_usuario.apellido_paterno} {obj.id_usuario.apellido_materno}, {obj.id_usuario.nombres}"
    
    def get_bibliotecario(self, obj):
        return obj.id_bibliotecario.nombres
    
    def get_estado_devolucion(self, obj):
        return obj.id_devolucion is not None
    
    class Meta:
        model = Prestamo
        fields = ['id_prestamo', 'fecha_prestamo', 'fecha_caducidad', 'usuario', 'bibliotecario', 'estado_devolucion', 'id_devolucion']
    
    