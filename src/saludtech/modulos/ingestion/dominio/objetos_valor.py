from __future__ import annotations

from dataclasses import dataclass, field
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class NombreRegion():
    nombre: str

@dataclass(frozen=True)
class Tipo(Enum):
    RAYOSX = "Rayos x"
    RESONANCIA = "Resonancia"
    HISTOPATOLOGIA = "Histopatologia"
    OTRO = "Otro"
    

@dataclass(frozen=True)
class Imagen(ObjetoValor):
    tipo : Tipo
    archivo : str
    def tipo(self)-> Enum:
        return self.tipo
    def archivo(self)-> str:
        return self.archivo