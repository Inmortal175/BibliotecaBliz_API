from rest_framework.viewsets import ModelViewSet
from ..Serializer.reporte_usuario_serializer import RepoprteUsuarioModelSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, F, Value
from django.db.models.functions import Concat

from ..Models.usuario_model import UsuarioBiblioteca

from ..pagination.custom_pagination import CustomPageNumberPagination

from rest_framework import filters
from django.utils.dateparse import parse_date

class ReporteUsuarioModelViewSet(ModelViewSet):
    serializer_class = RepoprteUsuarioModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset =  UsuarioBiblioteca.objects.annotate(
            cant_prestamos=Count('prestamo'),
            agregado_por=Concat(
                F('id_bibliotecario__nombres'), 
                Value(', '), 
                F('id_bibliotecario__apellido_paterno'), 
                Value(' '), 
                F('id_bibliotecario__apellido_materno')
            )
        ).order_by('nombres')
        
        # Obtener los valores de fecha_inicio y fecha_fin de los query_params
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')
        
        # Obtener el id del bibliotecario de los query_params
        bibliotecario = self.request.query_params.get('bibliotecario')

        # Filtrar el queryset si se proporcionan ambas fechas
        if fecha_inicio and fecha_fin:
            fecha_inicio = parse_date(fecha_inicio)
            fecha_fin = parse_date(fecha_fin)
            queryset = queryset.filter(fecha_creacion__range=[fecha_inicio, fecha_fin])
        
        # Filtrar el queryset por id de bibliotecario si se proporciona
        if bibliotecario:
            queryset = queryset.filter(id_bibliotecario__nombres=bibliotecario)

        return queryset