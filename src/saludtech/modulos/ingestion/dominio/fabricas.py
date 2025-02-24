from .excepciones import TipoObjetoNoExisteEnDominioIngestionExcepcion
from .entidades import ProcesoIngestion
from saludtech.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaProcesoIngestion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            proceso_ingestion: ProcesoIngestion = mapeador.dto_a_entidad(obj)

            return proceso_ingestion

@dataclass
class FabricaIngestion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ProcesoIngestion.__class__:
            fabrica_ingestion = _FabricaProcesoIngestion()
            return fabrica_ingestion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioIngestionExcepcion()