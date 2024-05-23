from rest_framework.viewsets import ModelViewSet
from ..Serializer.prestamo_serializer import PrestamoModelSerializer, PrestamoCreateModelSerializer
from ..Models.prestamo_model import Prestamo

from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from ..pagination.custom_pagination import CustomPageNumberPagination

class PrestamoModelViewSet(ModelViewSet):
    serializer_class = PrestamoModelSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['id_usuario__nombres', 'id_usuario__apellido_paterno', 'id_usuario__apellido_materno',]
    queryset = Prestamo.objects.all()
    pagination_class = CustomPageNumberPagination
    
class PrestamoCreateModelViewSet(ModelViewSet):
    serializer_class = PrestamoCreateModelSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    queryset = Prestamo.objects.all()    