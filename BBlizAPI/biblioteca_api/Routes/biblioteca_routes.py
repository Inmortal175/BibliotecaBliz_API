from rest_framework.routers import DefaultRouter

# importacion de Model View Set
from ..Views.reporte_prestamos_view import ReportePrestamoModelViewSet

#importar ModelViewSets
from bibliotecario.views import RegisterViewSet, BibliotecarioModelViewSet
from ..Views.usuario_view import UsuarioModelViewSet, CreateModelViewSet

from ..Views.prestamo_view import PrestamoModelViewSet, PrestamoCreateModelViewSet

from ..Views.detalle_prestamo_view import  DetallePrestamoCreateModelViewSet, DetallePrestamoModelViewSet

from ..Views.reporte_usuario_view import ReporteUsuarioModelViewSet

from ..Views.resporte_devoluciones_view import ReposrteDevolucionModelViewSet
# con DefaultRouter se puede crear diferentes rutas esta vez solo usaremos esta ruta
from ..Views.autor_view import AutorModelViewSet
from ..Views.genero_view import GeneroModelViewSet
from ..Views.libro_view import LibroModelViewSet
from ..Views.proveedor_view import ProveedorModelViewSet
from ..Views.publica_view import PublicaModelViewSet
from ..Views.nacionalidad_view import NacionalidadModelViewSet

# editorial
from ..Views.editorial_view import EditorialModelViewSet

routes: DefaultRouter = DefaultRouter()
routes.register(prefix='reporte_prestamo', basename= "reportes de prestamos de libro", viewset=ReportePrestamoModelViewSet)
routes.register(prefix='reporte_usuario', basename= "reportes de usuarios", viewset=ReporteUsuarioModelViewSet)
routes.register(prefix='reporte_devoluciones', basename= "reportes de devoluciones", viewset=ReposrteDevolucionModelViewSet)
# routes.register(prefix='Libros', basename=, viewset=)
routes.register(prefix='bibliotecario/register', basename='bibliotecario_register', viewset=RegisterViewSet) # ruta desde bibliotecario
routes.register(prefix='bibliotecario/view', basename='bibliotecario', viewset=BibliotecarioModelViewSet) # ruta desde bibliotecario
# La línea `routes.register(prefix='usuario', basename='usuarios', viewset=UsuarioModelViewSet)` está
# registrando un patrón de URL para el conjunto de vistas `UsuarioModelViewSet` bajo el prefijo
# `usuario`.
routes.register(prefix='usuario', basename='usuario', viewset=UsuarioModelViewSet)
routes.register(prefix='create/usuario', basename='create usuario', viewset=CreateModelViewSet)

#prestamo
routes.register(prefix='create/prestamo', basename='create prestamo', viewset=PrestamoCreateModelViewSet)
routes.register(prefix='prestamo', basename='prestamo', viewset=PrestamoModelViewSet)

#detalle prestamo
routes.register(prefix='detalle_prestamo', basename='detalle prestamo', viewset=DetallePrestamoModelViewSet)
routes.register(prefix='create/detalle_prestamo', basename='detalle_prestamo', viewset= DetallePrestamoCreateModelViewSet)


# Rutas para autor, genero, libro, proveedor y publica
routes.register(prefix="autor", viewset=AutorModelViewSet)
routes.register(prefix="genero", viewset=GeneroModelViewSet)
routes.register(prefix="libro", viewset=LibroModelViewSet)
routes.register(prefix="proveedor", viewset=ProveedorModelViewSet)
routes.register(prefix="publica",basename="publica_libro", viewset=PublicaModelViewSet)
routes.register(prefix="nacionalidad", basename='nacionalidad',  viewset=NacionalidadModelViewSet)

# ruta para la editorial
routes.register('editoriales', basename='editoriales', viewset=EditorialModelViewSet)