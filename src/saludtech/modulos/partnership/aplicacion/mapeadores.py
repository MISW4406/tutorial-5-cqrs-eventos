from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.seedwork.dominio.repositorios import Mapeador
from .dto import ProcesoIngestionPartnerDTO
from saludtech.modulos.partnership.dominio.entidades import ProcesoIngestionPartner



class MapeadorProcesoIngestionPartnerDTOJson(AppMap):  

    def externo_a_dto(self, externo: dict) -> ProcesoIngestionPartnerDTO:
        proceso_ingestion_partner_dto = ProcesoIngestionPartnerDTO()
        proceso_ingestion_partner_dto.id_partner = externo.get('id_partner')
        proceso_ingestion_partner_dto.id_proceso_ingestion = externo.get('id_proceso_ingestion')

        return proceso_ingestion_partner_dto
    def dto_a_externo(self, dto: ProcesoIngestionPartnerDTO) -> dict:
        return dto.__dict__
class MapeadorProcesoIngestionPartner(RepMap):
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
        proceso_ingestion_partner= ProcesoIngestionPartner()
        proceso_ingestion_partner.id_partner = dto.id_partner
        proceso_ingestion_partner.id_proceso_ingestion = dto.id_proceso_ingestion
        proceso_ingestion_partner.fecha_actualizacion = dto.fecha_actualizacion
        proceso_ingestion_partner.fecha_creacion = dto.fecha_creacion
        
        return proceso_ingestion_partner