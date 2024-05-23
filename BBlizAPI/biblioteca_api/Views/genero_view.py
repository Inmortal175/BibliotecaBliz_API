from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Modelo y serializador
from ..Models.genero_model import Genero
from ..Serializer.genero_serializer import GeneroModelSerializer


class GeneroModelViewSet(ModelViewSet):
    serializer_class = GeneroModelSerializer
    queryset = Genero.objects.all()
    