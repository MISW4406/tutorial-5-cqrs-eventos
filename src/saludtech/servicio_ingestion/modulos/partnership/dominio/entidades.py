from __future__ import annotations
from dataclasses import dataclass, field


from saludtech.servicio_ingestion.modulos.partnership.dominio.eventos import ProcesoIngestionPartnerAgregado
from saludtech.servicio_ingestion.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class ProcesoIngestionPartner(AgregacionRaiz):
    id_partner: uuid.UUID = field(hash=True, default=None)
    id_proceso_ingestion: uuid.UUID = field(hash=True, default=None)
    
    def agregar_proceso_ingestion_partner(self, proceso_ingestion_partner: ProcesoIngestionPartner):
        self.id_partner = proceso_ingestion_partner.id_partner
        self.id_proceso_ingestion = proceso_ingestion_partner.id_proceso_ingestion
    
        self.agregar_evento(ProcesoIngestionPartnerAgregado(id_proceso_ingestion=self.id, id_partner=self.id_partner, fecha_creacion=self.fecha_creacion))
