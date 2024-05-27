from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..pagination.custom_pagination import CustomPageNumberPagination
from rest_framework.filters import SearchFilter
from ..Serializer.detalle_prestamo_serializer import DetallePrestamoModelSerializer, DetallePrestamoCreateModelSerializer
from ..Models.detalle_prestamo_model import DetallePrestamo

    
# Esta clase define un conjunto de vistas para crear instancias del modelo DetallePrestamo con el
# método POST permitido para usuarios autenticados.
class DetallePrestamoCreateModelViewSet(ModelViewSet):
    serializer_class = DetallePrestamoCreateModelSerializer
    http_method_names = ['post',]
    permission_classes = [IsAuthenticated] 
    queryset = DetallePrestamo.objects.all()
    

# Esta clase es un ModelViewSet para manejar información de préstamo detallada con configuraciones
# específicas para métodos HTTP, permisos, filtrado, búsqueda, paginación y serialización.
class DetallePrestamoModelViewSet(ModelViewSet):
    serializer_class = DetallePrestamoModelSerializer
    http_method_names = ['get', 'Post']
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['id_prestamo__id_prestamo']    
    queryset = DetallePrestamo.objects.all()
    pagination_class = CustomPageNumberPagination