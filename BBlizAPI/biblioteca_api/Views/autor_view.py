from rest_framework.viewsets import ModelViewSet
# Modelo y serializador
from ..Models.autor_model import Autor
from ..Serializer.autor_serializer import AutorModelSerializer, AutorCreateModelSerializer
from rest_framework.filters import SearchFilter
from ..pagination.custom_pagination import CustomPageNumberPagination

from rest_framework.permissions import IsAuthenticated

class AutorModelViewSet(ModelViewSet):
    serializer_class = AutorModelSerializer
    filter_backends = [SearchFilter]
    pagination_class = CustomPageNumberPagination
    search_fields = ['nombres', 'id_nacionalidad__gentilicio',]
    queryset = Autor.objects.all()
    http_method_names = ['get']
    
class AutorCreateModelViewSet(ModelViewSet):
    serializer_class = AutorCreateModelSerializer
    queryset = Autor.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'put', 'delete']
  
  
    
    
    

