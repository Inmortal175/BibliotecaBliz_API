from django.contrib import admin

# Register your models here.
from .Models.autor_model            import Autor
from .Models.detalle_prestamo_model import DetallePrestamo
from .Models.devolucion_model       import Devolucion
from .Models.editorial_model        import Editorial
from .Models.genero_model           import Genero
from .Models.libro_model            import Libro
from .Models.nacionalidad_model     import Nacionalidad
from .Models.prestamo_model         import Prestamo
from .Models.proveedor_model        import Proveedor
from .Models.publica_model          import Publica
from .Models.usuario_model          import UsuarioBiblioteca
    # from .Models import 
    
@admin.register(
    Autor, 
    DetallePrestamo,
    Devolucion,
    Editorial,
    Genero,
    Libro,
    Nacionalidad,
    Prestamo,
    Proveedor,
    Publica,
    UsuarioBiblioteca
    )
class Admin (admin.ModelAdmin):
    pass
