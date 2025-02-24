from .entidades import ProcesoIngestionPartner
from .excepciones import TipoObjetoNoExisteEnDominioPartnershipExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
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
        if mapeador.obtener_tipo() == ProcesoIngestion.__class__:
            fabrica_proceso_ingestion_partner = _FabricaProcesoIngestionPartner()
            return fabrica_proceso_ingestion_partner.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPartnershipExcepcion()