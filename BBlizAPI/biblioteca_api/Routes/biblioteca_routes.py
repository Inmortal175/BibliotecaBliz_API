from rest_framework.routers import DefaultRouter

#importacion de Model View Set
from ..Views.reporte_prestamos_view import ReportePrestamoModelViewSet
from bibliotecario.views import RegisterViewSet

# con DefaultRouter se puede crear diferentes rutas esta vez solo usaremos esta ruta
routes : DefaultRouter = DefaultRouter()


routes.register(prefix='reporte_prestamo', basename= "reportes de prestamos de libro", viewset=ReportePrestamoModelViewSet)
# routes.register(prefix='Libros', basename=, viewset=)
routes.register(prefix='bibliotecario/register', basename='bibliotecario_register', viewset=RegisterViewSet) # ruta desde bibliotecario