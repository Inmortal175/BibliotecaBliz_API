from rest_framework.viewsets import ModelViewSet
from ..Models.devolucion_model import Devolucion

from ..Serializer.devolucion_serializer import DevolucionModelSerializer

class DevolucionModelViewSet(ModelViewSet):
    serializer_class = DevolucionModelSerializer
    queryset = Devolucion.objects.all()
    http_method_names = ['post']