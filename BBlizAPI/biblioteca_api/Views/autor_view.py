from rest_framework.viewsets import ModelViewSet
# Modelo y serializador
from ..Models.autor_model import Autor
from ..Serializer.autor_serializer import AutorModelSerializer
from ..pagination.custom_pagination import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class AutorModelViewSet(ModelViewSet):
    serializer_class = AutorModelSerializer
    queryset = Autor.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]
    
    
    
    

