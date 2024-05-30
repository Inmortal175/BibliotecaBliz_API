from rest_framework.serializers import ModelSerializer

from ..Models.devolucion_model import  Devolucion

class DevolucionModelSerializer( ModelSerializer):
    class Meta:
        model = Devolucion
        fields = '__all__'