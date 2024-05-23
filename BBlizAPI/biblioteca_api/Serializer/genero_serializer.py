from rest_framework.serializers import ModelSerializer
from ..Models.genero_model import Genero

class GeneroModelSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"