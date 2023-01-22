from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from dataclasses import dataclass
import uuid

@dataclass
class ObtenerReserva(Query):
    id_reserva: str

class ObtenerReservaHandler(QueryHandler):

    def handle(query: ObtenerReserva) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        reserva =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)