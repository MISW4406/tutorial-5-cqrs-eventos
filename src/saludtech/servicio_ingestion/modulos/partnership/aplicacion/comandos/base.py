from saludtech.servicio_ingestion.seedwork.aplicacion.comandos import ComandoHandler
from saludtech.servicio_ingestion.modulos.partnership.infraestructura.fabricas import FabricaRepositorio
from saludtech.servicio_ingestion.modulos.partnership.dominio.fabricas import FabricaPartnership

class AgregarProcesoIngestionPartnerBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_partnership: FabricaPartnership = FabricaPartnership()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_partnership(self):
        return self._fabrica_partnership   