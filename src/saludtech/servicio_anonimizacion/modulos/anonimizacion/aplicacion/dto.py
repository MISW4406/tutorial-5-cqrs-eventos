from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.aplicacion.dto import DTO

@dataclass()
class ImagenAnonimizadaDTO(DTO):
    tipo: str
    archivo: str
    archivo_anonimizado: str = None

@dataclass()
class ProcesoAnonimizacionDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    imagenes: list[ImagenAnonimizadaDTO] = field(default_factory=list)
    id_proceso_ingestion: str = field(default_factory=str)
    estado: str = field(default_factory=str)