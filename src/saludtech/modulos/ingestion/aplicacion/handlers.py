from saludtech.modulos.ingestion.dominio.eventos import ProcesoIngestionCreado
from saludtech.seedwork.aplicacion.handlers import Handler
from aeroalpes.modulos.vuelos.infraestructura.despachadores import Despachador

class HandlerProcesoIngestionIntegracion(Handler):

    @staticmethod
    def handle_proceso_ingestion_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-proceso_ingestion')



    