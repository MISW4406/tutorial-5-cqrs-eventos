from __future__ import annotations
from dataclasses import dataclass, field

import saludtech.servicio_ingestion.modulos.ingestion.dominio.objetos_valor as ov
from saludtech.servicio_ingestion.modulos.ingestion.dominio.eventos import ProcesoIngestionCreado
from saludtech.servicio_ingestion.seedwork.dominio.entidades import AgregacionRaiz, Entidad
@dataclass
class Region(Entidad):
    nombre: ov.NombreRegion = field(default_factory=ov.NombreRegion)
    def __str__(self) -> str:
        return self.nombre.nombre.upper()


@dataclass
class ProcesoIngestion(AgregacionRaiz):
    id_partner: uuid.UUID = field(hash=True, default=None)
    imagenes: list[ov.Imagen] = field(default_factory=list[ov.Imagen])
    #region: Region = field(default_factory=Region)
    def crear_proceso_ingestion(self, proceso_ingestion: ProcesoIngestion):
        self.id_partner = proceso_ingestion.id_partner
        self.imagenes = proceso_ingestion.imagenes
        #self.region = proceso_ingestion.region

        self.agregar_evento(ProcesoIngestionCreado(id_proceso_ingestion=self.id, id_partner=self.id_partner, fecha_creacion=self.fecha_creacion))

