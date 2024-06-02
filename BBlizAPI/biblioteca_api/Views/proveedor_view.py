from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..pagination.custom_pagination import CustomPageNumberPagination
# Modelo y serializador
from ..Models.proveedor_model import Proveedor
from ..Serializer.proveedor_serializer import ProveedorModelSerializer


class ProveedorModelViewSet(ModelViewSet):
    serializer_class = ProveedorModelSerializer
    queryset = Proveedor.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]