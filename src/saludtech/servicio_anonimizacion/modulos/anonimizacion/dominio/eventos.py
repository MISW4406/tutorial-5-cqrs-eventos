from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class ProcesoAnonimizacionCreado(EventoDominio):
    id_proceso_anonimizacion: uuid.UUID = None
    id_proceso_ingestion: uuid.UUID = None
    fecha_creacion: datetime = None

@dataclass
class ProcesoAnonimizacionCompletado(EventoDominio):
    id_proceso_anonimizacion: uuid.UUID = None
    id_proceso_ingestion: uuid.UUID = None
    fecha_actualizacion: datetime = None