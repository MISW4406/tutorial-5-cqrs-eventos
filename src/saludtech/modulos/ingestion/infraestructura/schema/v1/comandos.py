from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearProcesoIngestionPayload(ComandoIntegracion):
    id_partner=str()
    fecha_creacion= str()
    fecha_actualizacion= str()
    id_proceso_ingestion= str()
    imagenes= list()
    

class ComandoCrearProcesoIngestion(ComandoIntegracion):
    data = ComandoCrearProcesoIngestionPayload()