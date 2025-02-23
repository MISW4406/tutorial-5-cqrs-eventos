from __future__ import annotations
from dataclasses import dataclass, field

import saludtech.modulos.ingestion.dominio.objetos_valor as ov
from saludtech.modulos.vuelos.dominio.eventos import ProcesoIngestionCreado
from saludtech.seedwork.dominio.entidades import AgregacionRaiz, Entidad
@dataclass
class Region(Entidad):
    nombre: ov.NombreRegion = field(default_factory=ov.NombreRegion)
    def __str__(self) -> str:
        return self.nombre.nombre.upper()


@dataclass
class ProcesoIngestion(AgregacionRaiz):
    id_partner: uuid.UUID = field(hash=True, default=None)
    imagenes: list[ov.Imagen] = field(default_factory=list[ov.Imagen])
    region: Region = field(default_factory=Region)
    def crear_proceso_ingestion(self, proceso_ingestion: ProcesoIngestion):
        self.id_partner = proceso_ingestion.id_cliente
        self.imagenes = proceso_ingestion.imagenes
        self.region = proceso_ingestion.region

        self.agregar_evento(ProcesoIngestion(id_proceso_ingestion=self.id, id_partner=self.id_partner, fecha_creacion=self.fecha_creacion))

