from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando as comando
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.partnership.aplicacion.dto import ProcesoIngestionPartnerDTO
from .base import AgregarProcesoIngestionPartnerBaseHandler

from saludtech.modulos.partnership.dominio.entidades import ProcesoIngestionPartner
from saludtech.modulos.partnership.aplicacion.mapeadores import MapeadorProcesoIngestionPartner
from saludtech.modulos.partnership.infraestructura.repositorios import RepositorioProcesoIngestionPartner
from saludtech.modulos.partnership.infraestructura.despachadores import Despachador

@dataclass
class AgregarProcesoIngestionPartner(Comando):
    id_partner: str
    id_proceso_ingestion: str
    fecha_creacion: str
    fecha_actualizacion: str



class AgregarProcesoIngestionPartnerHandler(AgregarProcesoIngestionPartnerBaseHandler):
    def handle(self, comando: AgregarProcesoIngestionPartner):
        
        proceso_ingestion_partner_dto = ProcesoIngestionPartnerDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id_partner=comando.id_partner
            ,   id_proceso_ingestion=comando.id_proceso_ingestion)
        proceso_ingestion_partner: ProcesoIngestionPartner = self.fabrica_partnership.crear_objeto(proceso_ingestion_partner_dto, MapeadorProcesoIngestionPartner())
        proceso_ingestion_partner.agregar_proceso_ingestion_partner(proceso_ingestion_partner)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoIngestionPartner.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, proceso_ingestion_partner)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(AgregarProcesoIngestionPartner)
def ejecutar_comando_agregar_proceso_ingestion_partner(comando: AgregarProcesoIngestionPartner):
    
    handler = AgregarProcesoIngestionPartnerHandler()
    handler.handle(comando)
    