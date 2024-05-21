# views.py
# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .Serializer.bibliotecario_serializer import RegisterSerializer
from .models import Bibliotecario

class RegisterViewSet(ModelViewSet):
    queryset = Bibliotecario.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return Bibliotecario.objects.none()  # No listar usuarios

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

