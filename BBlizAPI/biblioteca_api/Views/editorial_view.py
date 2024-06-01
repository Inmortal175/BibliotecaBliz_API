from rest_framework.viewsets import ModelViewSet
# Modelo y serializador
from ..Models.editorial_model import Editorial
from ..Serializer.editorial_serializer import EditorialModelSerializer


class EditorialModelViewSet(ModelViewSet):
    serializer_class = EditorialModelSerializer
    queryset = Editorial.objects.all()
    