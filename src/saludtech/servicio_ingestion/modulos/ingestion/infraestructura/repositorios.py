from saludtech.servicio_ingestion.config.db import db
from saludtech.servicio_ingestion.modulos.ingestion.dominio.repositorios import RepositorioProcesoIngestion
from saludtech.servicio_ingestion.modulos.ingestion.dominio.entidades import ProcesoIngestion
from saludtech.servicio_ingestion.modulos.ingestion.dominio.fabricas import FabricaIngestion
from .dto import ProcesoIngestion as ProcesoIngestionDto
from .mapeadores import MapeadorProcesoIngestion
from uuid import UUID

class RepositorioProcesoIngestionPg(RepositorioProcesoIngestion):

    def __init__(self):
        self._fabrica_ingestion: FabricaIngestion = FabricaIngestion()

    @property
    def fabrica_ingestion(self):
        return self._fabrica_ingestion

    def obtener_por_id(self, id: UUID) -> ProcesoIngestion:
        proceso_ingestion_dto = db.session.query(ProcesoIngestionDto).filter_by(id=str(id)).one()
        return self._fabrica_ingestion.crear_objeto(proceso_ingestion_dto, MapeadorProcesoIngestion())

    def obtener_todos(self) -> list[ProcesoIngestion]:
        # TODO
        raise NotImplementedError

    def agregar(self, proceso_ingestion: ProcesoIngestion):
        proceso_ingestion_dto = self._fabrica_ingestion.crear_objeto(proceso_ingestion, MapeadorProcesoIngestion())
        db.session.add(proceso_ingestion_dto)

    def actualizar(self, proceso_ingestion: ProcesoIngestion):
        # TODO
        raise NotImplementedError

    def eliminar(self, proceso_ingestion_id: UUID):
        # TODO
        raise NotImplementedError