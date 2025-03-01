from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoProcesarAnonimizacionPayload(Record):
    id_proceso_ingestion = String()
    fecha_creacion = String()
    fecha_actualizacion = String()
    id_proceso_anonimizacion = String()
    imagenes = Array(object())
    estado = String()

class ComandoProcesarAnonimizacion(ComandoIntegracion):
    data = ComandoProcesarAnonimizacionPayload()