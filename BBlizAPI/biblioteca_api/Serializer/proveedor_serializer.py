from rest_framework.serializers import ModelSerializer
from ..Models.proveedor_model import Proveedor

class ProveedorModelSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"