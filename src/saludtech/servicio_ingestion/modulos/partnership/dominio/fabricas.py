from .entidades import ProcesoIngestionPartner
from .excepciones import TipoObjetoNoExisteEnDominioPartnershipExcepcion
from saludtech.servicio_ingestion.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtech.servicio_ingestion.seedwork.dominio.fabricas import Fabrica
from saludtech.servicio_ingestion.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaProcesoIngestionPartner(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            proceso_ingestion_partner: ProcesoIngestionPartner = mapeador.dto_a_entidad(obj)

            return proceso_ingestion_partner

@dataclass
class FabricaPartnership(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ProcesoIngestionPartner.__class__:
            fabrica_partnership = _FabricaProcesoIngestionPartner()
            return fabrica_partnership.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPartnershipExcepcion()