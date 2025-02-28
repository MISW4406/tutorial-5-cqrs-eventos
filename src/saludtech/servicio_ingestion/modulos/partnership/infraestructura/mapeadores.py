from saludtech.servicio_ingestion.seedwork.dominio.repositorios import Mapeador
from saludtech.servicio_ingestion.modulos.partnership.dominio.entidades import ProcesoIngestionPartner
from .dto import ProcesoIngestionPartner as ProcesoIngestionPartnerDTO


class MapeadorProcesoIngestionPartner(Mapeador):
   
    def obtener_tipo(self) -> type:
        return ProcesoIngestionPartner.__class__

    def entidad_a_dto(self, entidad: ProcesoIngestionPartner) -> ProcesoIngestionPartnerDTO:
        
        proceso_ingestion_partner_dto = ProcesoIngestionPartnerDTO()
        proceso_ingestion_partner_dto.fecha_creacion = entidad.fecha_creacion
        proceso_ingestion_partner_dto.fecha_actualizacion = entidad.fecha_actualizacion
        proceso_ingestion_partner_dto.id_partner = str(entidad.id_partner)
        proceso_ingestion_partner_dto.id_proceso_ingestion = str(entidad.id_proceso_ingestion)


        return proceso_ingestion_partner_dto

    def dto_a_entidad(self, dto: ProcesoIngestionPartnerDTO) -> ProcesoIngestionPartner:
        proceso_ingestion_partner = ProcesoIngestionPartner(dto.id_partner,dto.id_proceso_ingestion, dto.fecha_creacion, dto.fecha_actualizacion)
        
        return proceso_ingestion