from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoAnonimizarProcesoPayload(Record):
    id_proceso_original = String()
    fecha_creacion = String()
    fecha_actualizacion = String()
    id_proceso_anonimizacion = String()
    imagenes = Array(Map(String()))

class ComandoAnonimizarProceso(ComandoIntegracion):
    data = ComandoAnonimizarProcesoPayload()