from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerReservasNoPagadas(Query):
    listing_id: uuid.UUID

class ObtenerReservasNoPagadasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...