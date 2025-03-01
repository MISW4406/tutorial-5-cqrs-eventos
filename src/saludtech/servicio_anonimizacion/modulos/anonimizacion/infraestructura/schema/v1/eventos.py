from pulsar.schema import *
from saludtech.servicio_anonimizacion.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProcesoAnonimizacionCreadoPayload(Record):
    id_proceso_anonimizacion = String()
    id_proceso_ingestion = String()
    fecha_creacion = Long()

class EventoProcesoAnonimizacionCreado(EventoIntegracion):
    data = ProcesoAnonimizacionCreadoPayload()

class ProcesoAnonimizacionCompletadoPayload(Record):
    id_proceso_anonimizacion = String()
    id_proceso_ingestion = String()
    fecha_actualizacion = Long()

class EventoProcesoAnonimizacionCompletado(EventoIntegracion):
    data = ProcesoAnonimizacionCompletadoPayload()