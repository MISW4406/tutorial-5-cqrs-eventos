from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ProcesoIngestionPartnerAgregado(EventoDominio):
    id_proceso_ingestion: uuid.UUID = None
    id_partner: uuid.UUID = None
    fecha_creacion: datetime = None