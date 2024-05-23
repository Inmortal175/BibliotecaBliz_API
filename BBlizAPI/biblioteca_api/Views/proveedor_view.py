from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Modelo y serializador
from ..Models.proveedor_model import Proveedor
from ..Serializer.proveedor_serializer import ProveedorModelSerializer


class ProveedorModelViewSet(ModelViewSet):
    serializer_class = ProveedorModelSerializer
    queryset = Proveedor.objects.all()
    