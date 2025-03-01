from __future__ import annotations

from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class EstadoAnonimizacion(ObjetoValor):
    estado: str = "PENDIENTE"  # PENDIENTE, PROCESANDO, COMPLETADO, FALLIDO
    
@dataclass(frozen=True)
class ImagenAnonimizada(ObjetoValor):
    tipo: str
    archivo: str
    archivo_anonimizado: str = None