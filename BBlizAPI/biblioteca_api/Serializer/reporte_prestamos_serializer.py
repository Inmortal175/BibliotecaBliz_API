from rest_framework.serializers import ModelSerializer
from ..Models.prestamo_model import Prestamo

class ReportePrestamoModelSerializer(ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"