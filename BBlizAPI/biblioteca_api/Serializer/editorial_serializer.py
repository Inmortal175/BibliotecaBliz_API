from ..Models.editorial_model import Editorial
from rest_framework.serializers import ModelSerializer


class EditorialSerializer(ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'