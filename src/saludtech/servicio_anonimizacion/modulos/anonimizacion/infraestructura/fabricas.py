from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.dominio.fabricas import Fabrica
from saludtech.servicio_anonimizacion.seedwork.dominio.repositorios import Repositorio
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.repositorios import RepositorioProcesoAnonimizacion
from .repositorios import RepositorioProcesoAnonimizacionPg
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProcesoAnonimizacion.__class__:
            return RepositorioProcesoAnonimizacionPg()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()