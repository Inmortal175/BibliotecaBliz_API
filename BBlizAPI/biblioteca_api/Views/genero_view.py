from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..pagination.custom_pagination import CustomPageNumberPagination
# Modelo y serializador
from ..Models.genero_model import Genero
from ..Serializer.genero_serializer import GeneroModelSerializer


class GeneroModelViewSet(ModelViewSet):
    serializer_class = GeneroModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Genero.objects.all()
    pagination_class = CustomPageNumberPagination