# views.py
# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticated
from .Serializer.bibliotecario_serializer import RegisterSerializer
from .models import Bibliotecario

class RegisterViewSet(ModelViewSet):
    queryset = Bibliotecario.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    
    http_method_names = ['post']

    def get_queryset(self):
        return Bibliotecario.objects.none()  # No listar usuarios

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

