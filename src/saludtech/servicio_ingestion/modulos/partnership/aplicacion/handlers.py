from saludtech.servicio_ingestion.modulos.partnership.dominio.eventos import ProcesoIngestionPartnerAgregado
from saludtech.servicio_ingestion.seedwork.aplicacion.handlers import Handler
from saludtech.servicio_ingestion.modulos.partnership.infraestructura.despachadores import Despachador

class HandlerProcesoIngestionPartnerIntegracion(Handler):

    @staticmethod
    def handle_proceso_ingestion_partner_agregado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-proceso_ingestion_partner')

