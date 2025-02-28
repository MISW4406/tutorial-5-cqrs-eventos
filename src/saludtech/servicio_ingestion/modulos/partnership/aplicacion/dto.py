from dataclasses import dataclass, field
from saludtech.servicio_ingestion.seedwork.aplicacion.dto import DTO


@dataclass()
class ProcesoIngestionPartnerDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id_partner: str = field(default_factory=str)
    id_proceso_ingestion: str = field(default_factory=str)
