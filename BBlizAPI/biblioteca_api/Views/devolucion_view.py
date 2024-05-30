from rest_framework.viewsets import ModelViewSet
from ..Models.devolucion_model import Devolucion

from ..Serializer.devolucion_serializer import DevolucionModelSerializer
from rest_framework.permissions import IsAuthenticated

class DevolucionModelViewSet(ModelViewSet):
    serializer_class = DevolucionModelSerializer
    queryset = Devolucion.objects.all()
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]