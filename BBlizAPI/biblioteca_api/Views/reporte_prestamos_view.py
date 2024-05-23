from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
# importamos los modelo y la serilizadores
from ..Models.prestamo_model import Prestamo
from ..Serializer.reporte_prestamos_serializer import ReportePrestamoModelSerializer

from django.db import connection

from datetime import datetime

# Esta clase es un Django ModelViewSet para generar un informe sobre libros prestados en función de
# parámetros de consulta específicos.
class ReportePrestamoModelViewSet(ModelViewSet):
    serializer_class = ReportePrestamoModelSerializer
    queryset = Prestamo.objects.all()
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        # prestamo = ReportePrestamoModelSerializer(Prestamo.objects.all(), many = True)
        usuario : str = self.request.query_params.get('usuario', None)
        libro : str = self.request.query_params.get('title', None)
        bibliotecario : str = self.request.query_params.get('bibliotecario', None)
        fecha_inicio : str = self.request.query_params.get('fecha_inicio', None)
        fecha_limite : str = self.request.query_params.get('fecha_limite', None)
        SQL_WHERE :str = "WHERE 1=1 "
        if usuario:
            SQL_WHERE += "AND U.nombres = %s" % "'" + usuario + "'"      
        if libro:
            SQL_WHERE += " AND L.titulo = %s" % "'" + libro + "'"
        if bibliotecario:
            SQL_WHERE += " B.nombres = %s" % "'" + bibliotecario + "'"
        if fecha_inicio:
            SQL_WHERE += " AND pres.fecha_prestamo BETWEEN %s AND %s" % ("'" + str(fecha_inicio) + "'", "'" + str(fecha_limite) + "'")
        # consulta SQL para filtro y reporte
        with connection.cursor() as cursor:
            query = f"""
                SELECT 
                    CONCAT (U.nombres, ', ', U.apellido_paterno, ' ', U.apellido_materno) as usuario,
                    pres.fecha_prestamo,
                    L.titulo as Libro_prestado,
                    G.nombre as Genero_libro,
                    CONCAT (B.nombres, ' ', B.apellido_paterno, ' ', B.apellido_materno) as Bibliotecario,
                    CASE 
                        WHEN pres.id_devolucion_id IS NOT NULL THEN 'Devuelto'
                        ELSE 'por devolver'
                    END as Estado_Devolucion,
                    CASE
                        WHEN cast((pres.fecha_caducidad - cast('{datetime.now().date()}' as date)) as int) <= 0
                            THEN (CAST (CAST((pres.fecha_caducidad - cast('{datetime.now().date()}' as date)) as int)*(-1) as int) || ' días de retraso')  
                            ELSE (CAST((pres.fecha_caducidad - cast('{datetime.now().date()}' as date)) as int) || ' dias restantes')
                    END as retraso,
					pres.fecha_caducidad
                FROM 
                    biblioteca_api_usuariobiblioteca as U
                LEFT JOIN biblioteca_api_prestamo as pres ON U.id_usuario = pres.id_usuario_id
                LEFT JOIN biblioteca_api_detalleprestamo as det_p ON pres.id_prestamo = det_p.id_prestamo_id
                LEFT JOIN biblioteca_api_libro as L ON L.id_libro = det_p.id_libro_id
                LEFT JOIN biblioteca_api_genero as G ON G.id_genero = L.id_genero_id
                JOIN bibliotecario_bibliotecario as B ON B.id =pres.id_bibliotecario_id
                {SQL_WHERE}
                ORDER BY U.nombres ASC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                return Response({"error": "No se encontraron resultados para los parámetros dados."}, status=status.HTTP_404_NOT_FOUND)
            DATA = [ {
                'usuario'          : dato[0],
                'fecha_prestamo'   : dato[1],
                'libro'            : dato[2],
                'genero_libro'     : dato[3],
                'bibliotecario'    : dato[4],
                'estado_devolucion': dato[5],
                'retraso'          : dato[6],
                'fecha_caducidad'  : dato[7],
                } for dato in rows]

        return Response (DATA, status=status.HTTP_200_OK)