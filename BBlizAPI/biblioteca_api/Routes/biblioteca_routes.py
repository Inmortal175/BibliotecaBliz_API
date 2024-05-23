from rest_framework.routers import DefaultRouter

# importacion de Model View Set
from ..Views.reporte_prestamos_view import ReportePrestamoModelViewSet
from ..Views.autor_view import AutorModelViewSet
from ..Views.genero_view import GeneroModelViewSet
from ..Views.libro_view import LibroModelViewSet
from ..Views.proveedor_view import ProveedorModelViewSet
from ..Views.publica_view import PublicaModelViewSet
from ..Views.nacionalidad_view import NacionalidadModelViewSet

from bibliotecario.views import RegisterViewSet

# con DefaultRouter se puede crear diferentes rutas esta vez solo usaremos esta ruta
routes: DefaultRouter = DefaultRouter()


routes.register(
    prefix="reporte_prestamo",
    basename="reportes de prestamos de libro",
    viewset=ReportePrestamoModelViewSet,
)
# routes.register(prefix='Libros', basename=, viewset=)
routes.register(
    prefix="bibliotecario/register",
    basename="bibliotecario_register",
    viewset=RegisterViewSet,
)  # ruta desde bibliotecario

# Rutas para autor, genero, libro, proveedor y publica
routes.register(prefix="autor", viewset=AutorModelViewSet)
routes.register(prefix="genero", viewset=GeneroModelViewSet)
routes.register(prefix="libro", viewset=LibroModelViewSet)
routes.register(prefix="proveedor", viewset=ProveedorModelViewSet)
routes.register(prefix="publica", viewset=PublicaModelViewSet)
routes.register(prefix="nacionalidad", viewset=NacionalidadModelViewSet)
