from pydispatch import dispatcher

from .handlers import HandlerProcesoIngestionIntegracion

from saludtech.modulos.ingestion.dominio.eventos import ProcesoIngestionCreado

dispatcher.connect(HandlerProcesoIngestionIntegracion.handle_proceso_ingestion_creado, signal=f'{ProcesoIngestionCreado.__name__}Integracion')
