from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerReserva(Query):
    listing_id: uuid.UUID

class ObtenerReservaHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...