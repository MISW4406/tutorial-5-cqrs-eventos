from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerReservasCanceladas(Query):
    listing_id: uuid.UUID

class ObtenerReservasCanceladasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...