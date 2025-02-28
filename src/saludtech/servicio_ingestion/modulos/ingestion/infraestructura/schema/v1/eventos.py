from pulsar.schema import *
from saludtech.servicio_ingestion.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProcesoIngestionCreadoPayload(Record):
    id_proceso_ingestion = String()
    id_partner = String()
    fecha_creacion = Long()

class EventoProcesoIngestionCreado(EventoIntegracion):
    data = ProcesoIngestionCreadoPayload()