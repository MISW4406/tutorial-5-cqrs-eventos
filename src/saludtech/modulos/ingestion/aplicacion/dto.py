from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenDTO(DTO):
    tipo: str
    archivo: str

@dataclass(frozen=True)
class ProcesoIngestionDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    imagenes: list[ImagenDTO] = field(default_factory=list)
    id_partner: str = field(default_factory=str)
