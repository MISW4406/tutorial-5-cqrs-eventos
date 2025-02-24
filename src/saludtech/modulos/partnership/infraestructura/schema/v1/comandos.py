from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoAgregarProcesoIngestionPartnerPayload(ComandoIntegracion):
    id_partner=str()
    id_proceso_ingestion= str()
    fecha_creacion= str()
    fecha_actualizacion= str()

    

class ComandoAgregarProcesoIngestionPartner(ComandoIntegracion):
    data = ComandoAgregarProcesoIngestionPartnerPayload()