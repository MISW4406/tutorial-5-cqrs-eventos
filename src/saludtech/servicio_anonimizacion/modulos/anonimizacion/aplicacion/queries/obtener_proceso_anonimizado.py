from saludtech.servicio_anonimizacion.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.servicio_anonimizacion.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.repositorios import RepositorioProcesoAnonimizacion
from dataclasses import dataclass
from .base import ProcesoAnonimizacionQueryBaseHandler
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.mapeadores import MapeadorProcesoAnonimizacion
import uuid

@dataclass
class ObtenerProcesoAnonimizado(Query):
    id: str

class ObtenerProcesoAnonimizadoHandler(ProcesoAnonimizacionQueryBaseHandler):
    def handle(self, query: ObtenerProcesoAnonimizado) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoAnonimizacion.__class__)
        proceso_anonimizacion = self.fabrica_anonimizacion.crear_objeto(
            repositorio.obtener_por_id(query.id), 
            MapeadorProcesoAnonimizacion()
        )
        return QueryResultado(resultado=proceso_anonimizacion)

@query.register(ObtenerProcesoAnonimizado)
def ejecutar_query_obtener_proceso_anonimizado(query: ObtenerProcesoAnonimizado):
    handler = ObtenerProcesoAnonimizadoHandler()
    return handler.handle(query)