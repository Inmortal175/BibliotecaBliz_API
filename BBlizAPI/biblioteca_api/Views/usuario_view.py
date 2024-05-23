from rest_framework.viewsets import ModelViewSet
from ..Models.usuario_model import UsuarioBiblioteca
from rest_framework.permissions import IsAuthenticated
from ..Serializer.usuario_serializer import UsuarioModelSerializer, UsuarioCreatedSerializer

from rest_framework import status
from rest_framework.response import Response

from ..pagination.custom_pagination import CustomPageNumberPagination

from rest_framework.filters import SearchFilter

class UsuarioModelViewSet(ModelViewSet):
    serializer_class = UsuarioModelSerializer
    queryset = UsuarioBiblioteca.objects.all().select_related('id_bibliotecario').order_by('id_usuario')
    filter_backends = [SearchFilter]
    search_fields = ['nombres',]
    pagination_class = CustomPageNumberPagination
    http_method_names = ['put','get', 'delete']
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioCreatedSerializer
    queryset = UsuarioBiblioteca.objects.all()
    http_method_names = ['post']
    
    