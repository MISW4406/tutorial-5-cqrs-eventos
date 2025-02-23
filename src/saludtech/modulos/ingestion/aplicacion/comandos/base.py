from saludtech.seedwork.aplicacion.comandos import ComandoHandler
from saludtech.modulos.ingestion.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.ingestion.dominio.fabricas import FabricaIngestion

class CrearProcesoIngestionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion   