from dataclasses import dataclass, field
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.partnership.dominio.repositorios import RepositorioProcesoIngestionPartner
from .repositorios import RepositorioProcesoIngestionPartnerPg
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProcesoIngestionPartner.__class__:
            return RepositorioProcesoIngestionPartnerPg()
        else:
            raise ExcepcionFabrica()