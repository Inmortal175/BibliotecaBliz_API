from rest_framework.viewsets import ModelViewSet

# Modelo y serializador
from ..Models.nacionalidad_model import Nacionalidad
from ..Serializer.nacionalidad_serializer import NacionalidadModelSerializer


class NacionalidadModelViewSet(ModelViewSet):
    serializer_class = NacionalidadModelSerializer
    queryset = Nacionalidad.objects.all()
