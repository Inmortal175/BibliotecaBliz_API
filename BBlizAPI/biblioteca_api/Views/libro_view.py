from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

# Modelo y serializador
from ..Models.libro_model import Libro
from ..Serializer.libro_serializer import LibroModelSerializer


class LibroModelViewSet(ModelViewSet):

    serializer_class = LibroModelSerializer
    queryset = Libro.objects.annotate(prestados=Count("detalleprestamos")).order_by(
        "id_libro"
    )
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
