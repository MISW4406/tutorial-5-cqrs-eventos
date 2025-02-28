from dataclasses import dataclass, field
from saludtech.servicio_ingestion.seedwork.dominio.fabricas import Fabrica
from saludtech.servicio_ingestion.seedwork.dominio.repositorios import Repositorio
from saludtech.servicio_ingestion.modulos.ingestion.dominio.repositorios import RepositorioProcesoIngestion
from .repositorios import RepositorioProcesoIngestionPg
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProcesoIngestion.__class__:
            return RepositorioProcesoIngestionPg()
        else:
            raise ExcepcionFabrica()