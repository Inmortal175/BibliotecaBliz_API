from rest_framework.serializers import ModelSerializer
from ..Models.usuario_model import UsuarioBiblioteca 
from ..Models.prestamo_model import Prestamo
from ..Models.detalle_prestamo_model import DetallePrestamo #,Devolucion#, 
from ..Models.libro_model import Libro

from rest_framework import serializers

class ReporteDevModelSerializer(ModelSerializer):
    libro = serializers.SerializerMethodField()
    nombres = serializers.SerializerMethodField()
    apellido_paterno = serializers.SerializerMethodField()
    apellido_materno = serializers.SerializerMethodField()
    bibliotecario = serializers.SerializerMethodField()
    fecha_devolucion = serializers.SerializerMethodField()
    
    def get_libro(self, obj):
        return obj.id_libro.titulo
    
    def get_nombres(self, obj):
        return obj.id_prestamo.id_usuario.nombres
    
    def get_apellido_paterno(self, obj):
        return obj.id_prestamo.id_usuario.apellido_paterno
    
    def get_apellido_materno(self, obj):
        return obj.id_prestamo.id_usuario.apellido_materno
    
    def get_bibliotecario(self, obj):
        return f"{obj.id_prestamo.id_bibliotecario.apellido_paterno} {obj.id_prestamo.id_bibliotecario.apellido_materno}, {obj.id_prestamo.id_bibliotecario.nombres}"
    
    def get_fecha_devolucion(self, obj):
        return obj.id_prestamo.id_devolucion.fecha_devolucion
    
    
    class Meta:
        model = DetallePrestamo
        fields = [
                "libro",
                "nombres",
                "apellido_paterno",
                "apellido_materno",
                "bibliotecario",
                "fecha_devolucion",
                ]