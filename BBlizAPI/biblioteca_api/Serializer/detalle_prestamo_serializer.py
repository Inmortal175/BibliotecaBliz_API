from rest_framework.serializers import ModelSerializer
from ..Models.detalle_prestamo_model import DetallePrestamo
from rest_framework import serializers

        
class DetallePrestamoCreateModelSerializer(ModelSerializer):
    class Meta:
        model = DetallePrestamo
        fields = '__all__'
    
class DetallePrestamoModelSerializer(ModelSerializer):
    titulo = serializers.SerializerMethodField()
    autor = serializers.SerializerMethodField()
    genero = serializers.SerializerMethodField()
    
    def get_titulo(self, obj):
        return obj.id_libro.titulo
    
    def get_autor(self, obj):
        return obj.id_libro.id_autor.nombres
    
    def get_genero(self, obj):
        return obj.id_libro.id_genero.nombre
    
    class Meta:
        model = DetallePrestamo
        fields = ['titulo', 'autor', 'genero']