from __future__ import annotations

from dataclasses import dataclass, field
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class NombreRegion():
    nombre: str
    

@dataclass(frozen=True)
class Imagen(ObjetoValor):
    tipo : str
    archivo : str
    def tipo(self)-> str:
        return self.tipo
    def archivo(self)-> str:
        return self.archivo