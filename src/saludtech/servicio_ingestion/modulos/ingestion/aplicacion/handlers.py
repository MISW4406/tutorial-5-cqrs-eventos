from saludtech.servicio_ingestion.modulos.ingestion.dominio.eventos import ProcesoIngestionCreado
from saludtech.servicio_ingestion.seedwork.aplicacion.handlers import Handler
from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.despachadores import Despachador

class HandlerProcesoIngestionIntegracion(Handler):

    @staticmethod
    def handle_proceso_ingestion_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-proceso_ingestion')



    