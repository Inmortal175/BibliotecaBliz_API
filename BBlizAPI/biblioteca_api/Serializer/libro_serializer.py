from rest_framework.serializers import ModelSerializer
from ..Models.libro_model import Libro

from ..Models.publica_model import Publica

from rest_framework import serializers
class PublicaSerializer(ModelSerializer):
    prestados = serializers.IntegerField(read_only=True)
    devuelto = serializers.IntegerField(read_only=True)
    
    id = serializers.SerializerMethodField()
    titulo = serializers.SerializerMethodField()
    editorial = serializers.SerializerMethodField()
    autor = serializers.SerializerMethodField()
    genero = serializers.SerializerMethodField()
    anio_publicacion = serializers.SerializerMethodField()
    cantidad = serializers.SerializerMethodField()
    descripcion = serializers.SerializerMethodField()    
    id_proveedor = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return obj.id_libro.id_libro
    
    def get_titulo(self, obj):
        return obj.id_libro.titulo
    
    def get_editorial(self, obj):
        return obj.id_editorial.nombre
    
    def get_autor(self, obj):
        return f"{obj.id_libro.id_autor.nombres} {obj.id_libro.id_autor.apellido_paterno}"
    
    def get_genero(self, obj):
        return obj.id_libro.id_genero.nombre
    
    def get_anio_publicacion(self, obj):
        return obj.id_libro.anio_publicacion
    
    def get_cantidad(self, obj):
        return obj.id_libro.cantidad
    
    def get_descripcion(self, obj):
        return obj.id_libro.descripcion
    
    def get_id_proveedor(self, obj):
        return obj.id_libro.id_proveedor.id_proveedor
    
    class Meta:
        model = Publica
        fields = ['id', 'titulo', 'genero', 'anio_publicacion', 'autor', 'editorial', 'cantidad', 'descripcion', 'prestados', 'devuelto', 'id_proveedor']


class LibroCreateSerializer(ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'