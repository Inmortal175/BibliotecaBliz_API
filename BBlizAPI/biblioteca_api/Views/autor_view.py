from rest_framework.viewsets import ModelViewSet
# Modelo y serializador
from ..Models.autor_model import Autor
from ..Serializer.autor_serializer import AutorModelSerializer


class AutorModelViewSet(ModelViewSet):
    serializer_class = AutorModelSerializer
    queryset = Autor.objects.all()
    
    
    

