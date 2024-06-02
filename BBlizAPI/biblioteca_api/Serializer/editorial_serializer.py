from rest_framework.serializers import ModelSerializer
from ..Models.editorial_model import Editorial

class EditorialModelSerializer(ModelSerializer):
    class Meta:
        model = Editorial
        fields = "__all__"