from rest_framework.serializers import ModelSerializer
from ..Models.nacionalidad_model import Nacionalidad

class NacionalidadModelSerializer(ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = "__all__"