from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.ingestion.infraestructura.repositorios import RepositorioProcesoIngestion
from dataclasses import dataclass
from .base import ProcesoIngestionQueryBaseHandler
from saludtech.modulos.ingestion.aplicacion.mapeadores import MapeadorProcesoIngestion
import uuid

@dataclass
class ObtenerProcesoIngestion(Query):
    id: str

class ObtenerProcesoIngestionHandler(ProcesoIngestionQueryBaseHandler):

    def handle(self, query: ObtenerProcesoIngestion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoIngestion.__class__)
        proceso_ingestion =  self.fabrica_ingestion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorProcesoIngestion())
        return QueryResultado(resultado=proceso_ingestion)

@query.register(ObtenerProcesoIngestion)
def ejecutar_query_Obtener_proceso_ingestion(query: ObtenerProcesoIngestion):
    handler = ObtenerProcesoIngestionHandler()
    return handler.handle(query)