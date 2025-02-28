from saludtech.servicio_ingestion.seedwork.aplicacion.queries import QueryHandler
from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from saludtech.servicio_ingestion.modulos.ingestion.dominio.fabricas import FabricaIngestion

class ProcesoIngestionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion    