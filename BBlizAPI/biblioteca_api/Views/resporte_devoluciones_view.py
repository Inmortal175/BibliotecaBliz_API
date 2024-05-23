from rest_framework.viewsets import ModelViewSet
from ..Models.detalle_prestamo_model import DetallePrestamo
from ..Serializer.reporte_devoluciones_serializer import ReporteDevModelSerializer

from  rest_framework.permissions import IsAuthenticated
class ReposrteDevolucionModelViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    queryset = DetallePrestamo.objects.all().filter(id_prestamo__id_devolucion__isnull=False)
    serializer_class = ReporteDevModelSerializer