from rest_framework.viewsets import ModelViewSet
from ..Models.editorial_model import Editorial
from ..pagination.custom_pagination import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated

from ..Serializer.editorial_serializer import EditorialModelSerializer

# from rest_framework.filters import

class EditorialModelViewSet(ModelViewSet):
    serializer_class = EditorialModelSerializer
    queryset = Editorial.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]
