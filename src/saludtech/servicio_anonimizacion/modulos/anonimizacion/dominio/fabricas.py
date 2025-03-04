from .excepciones import TipoObjetoNoExisteEnDominioAnonimizacionExcepcion
from .entidades import ProcesoAnonimizacion
from saludtech.servicio_anonimizacion.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtech.servicio_anonimizacion.seedwork.dominio.fabricas import Fabrica
from saludtech.servicio_anonimizacion.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaProcesoAnonimizacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            proceso_anonimizacion: ProcesoAnonimizacion = mapeador.dto_a_entidad(obj)
            return proceso_anonimizacion

@dataclass
class FabricaAnonimizacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ProcesoAnonimizacion.__class__:
            fabrica_anonimizacion = _FabricaProcesoAnonimizacion()
            return fabrica_anonimizacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAnonimizacionExcepcion()