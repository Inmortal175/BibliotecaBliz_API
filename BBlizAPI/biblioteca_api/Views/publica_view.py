from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Modelo y serializador
from ..Models.publica_model import Publica
from ..Serializer.publica_serializer import PublicaModelSerializer


class PublicaModelViewSet(ModelViewSet):
    serializer_class = PublicaModelSerializer
    queryset = Publica.objects.all()
    