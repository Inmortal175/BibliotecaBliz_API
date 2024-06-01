from rest_framework.viewsets import ModelViewSet
from ..Models.detalle_prestamo_model import DetallePrestamo
from ..Serializer.reporte_devoluciones_serializer import ReporteDevModelSerializer

from  rest_framework.permissions import IsAuthenticated
from ..pagination.custom_pagination import CustomPageNumberPagination
from django.utils.dateparse import parse_date
class ReposrteDevolucionModelViewSet(ModelViewSet):
    http_method_names = ['get']
    # permission_classes = [IsAuthenticated]
    serializer_class = ReporteDevModelSerializer
    pagination_class = CustomPageNumberPagination
    
    def get_queryset(self):
        queryset = DetallePrestamo.objects.all().filter(id_prestamo__id_devolucion__isnull=False)
        
        usuario = self.request.query_params.get('usuario')
        bibliotecario = self.request.query_params.get('bibliotecario')
        
        # Obtener los valores de fecha_inicio y fecha_fin de los query_params
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')

        # Filtrar el queryset si se proporcionan ambas fechas
        if fecha_inicio and fecha_fin:
            fecha_inicio = parse_date(fecha_inicio)
            fecha_fin = parse_date(fecha_fin)
            queryset = queryset.filter(id_prestamo__id_devolucion__fecha_devolucion__range=[fecha_inicio, fecha_fin])
        
        
        if usuario:
            queryset =  queryset.filter(id_prestamo__id_usuario__nombres = usuario)
        if bibliotecario:
            queryset = queryset.filter(id_prestamo__id_bibliotecario__nombres = bibliotecario)

        return queryset