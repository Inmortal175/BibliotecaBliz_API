from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

from ..pagination.custom_pagination import CustomPageNumberPagination
from rest_framework.filters import SearchFilter

from ..Serializer.libro_serializer import  PublicaSerializer, Publica, Libro, LibroCreateSerializer


class LibroModelViewSet(ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['id_libro__titulo', 'id_libro__id_genero__nombre', 'id_libro__id_autor__nombres']
    pagination_class = CustomPageNumberPagination
    http_method_names = ['get',]
    serializer_class = PublicaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Publica.objects.all()
    def get_queryset(self):
        queryset = Publica.objects.all().annotate(
            prestados=Count("id_libro__detalleprestamos"), 
            devuelto=Count('id_libro__detalleprestamos__id_prestamo__id_devolucion')
        ).order_by('id_libro__titulo')

        # Filtrar por título si se proporciona en los queryparams
        titulo = self.request.query_params.get('titulo', None)
        if titulo:
            queryset = queryset.filter(id_libro__titulo__icontains=titulo)
        
        # Filtrar por autor si se proporciona en los queryparams
        autor = self.request.query_params.get('autor', None)
        if autor:
            queryset = queryset.filter(id_libro__autor__icontains=autor)
        
        # Filtrar por genero si se proporciona en los queryparams
        genero = self.request.query_params.get('genero', None)
        if genero:
            queryset = queryset.filter(id_libro__genero__icontains=genero)

        return queryset

class LibroCreateModelViewSet(ModelViewSet):
    serializer_class = LibroCreateSerializer
    http_method_names = ['post', 'put', 'delete']
    queryset = Libro.objects.all()