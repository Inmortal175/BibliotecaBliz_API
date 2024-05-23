from rest_framework.viewsets import ModelViewSet

# Modelo y serializador
from ..Models.proveedor_model import Proveedor
from ..Serializer.proveedor_serializer import ProveedorModelSerializer


class NacionalidadModelViewSet(ModelViewSet):
    serializer_class = ProveedorModelSerializer
    queryset = Proveedor.objects.all()
