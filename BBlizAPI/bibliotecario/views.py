# views.py
# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticated
from .Serializer.bibliotecario_serializer import RegisterSerializer, BibliotecarioModelSerializer
from .models import Bibliotecario

from rest_framework.filters import SearchFilter

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

class RegisterViewSet(ModelViewSet):
    queryset = Bibliotecario.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    
    http_method_names = ['post']

    def get_queryset(self):
        return Bibliotecario.objects.none()  # No listar usuarios

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class BibliotecarioModelViewSet(ModelViewSet):
    serializer_class = BibliotecarioModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombres']
    permission_classes = [IsAuthenticated]
    queryset= Bibliotecario.objects.all()
    http_method_names = ['get']