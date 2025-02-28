from saludtech.servicio_ingestion.config.db import db
from saludtech.servicio_ingestion.modulos.partnership.dominio.repositorios import RepositorioProcesoIngestionPartner
from saludtech.servicio_ingestion.modulos.partnership.dominio.entidades import ProcesoIngestionPartner
from saludtech.servicio_ingestion.modulos.partnership.dominio.fabricas import FabricaPartnership
from .dto import ProcesoIngestionPartner as ProcesoIngestionPartnerDto
from .mapeadores import MapeadorProcesoIngestionPartner
from uuid import UUID

class RepositorioProcesoIngestionPartnerPg(RepositorioProcesoIngestionPartner):

    def __init__(self):
        self._fabrica_partnership: FabricaPartnership = FabricaPartnership()

    @property
    def fabrica_partnership(self):
        return self._fabrica_partnership

    def obtener_por_id(self, id: UUID) -> ProcesoIngestionPartner:
        proceso_ingestion_partner_dto = db.session.query(ProcesoIngestionPartnerDto).filter_by(id=str(id)).one()
        return self._fabrica_partnership.crear_objeto(proceso_ingestion_partner_dto, MapeadorProcesoIngestionPartner())

    def obtener_todos(self) -> list[ProcesoIngestionPartner]:
        # TODO
        raise NotImplementedError

    def agregar(self, proceso_ingestion_partner: ProcesoIngestionPartner):
        proceso_ingestion_partner_dto = self._fabrica_partnership.crear_objeto(proceso_ingestion_partner, MapeadorProcesoIngestionPartner())
        db.session.add(proceso_ingestion_partner_dto)

    def actualizar(self, proceso_ingestion_partner: ProcesoIngestionPartner):
        # TODO
        raise NotImplementedError

    def eliminar(self, proceso_ingestion_id: UUID):
        # TODO
        raise NotImplementedError