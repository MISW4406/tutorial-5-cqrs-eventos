from saludtech.servicio_anonimizacion.config.db import db
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.repositorios import RepositorioProcesoAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.entidades import ProcesoAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.fabricas import FabricaAnonimizacion
from .dto import ProcesoAnonimizacion as ProcesoAnonimizacionDTO
from .mapeadores import MapeadorProcesoAnonimizacion
from uuid import UUID

class RepositorioProcesoAnonimizacionPg(RepositorioProcesoAnonimizacion):
    def __init__(self):
        self._fabrica_anonimizacion: FabricaAnonimizacion = FabricaAnonimizacion()

    @property
    def fabrica_anonimizacion(self):
        return self._fabrica_anonimizacion

    def obtener_por_id(self, id: UUID) -> ProcesoAnonimizacion:
        proceso_anonimizacion_dto = db.session.query(ProcesoAnonimizacionDTO).filter_by(id=str(id)).one()
        return self._fabrica_anonimizacion.crear_objeto(proceso_anonimizacion_dto, MapeadorProcesoAnonimizacion())

    def obtener_todos(self) -> list[ProcesoAnonimizacion]:
        # TODO: Implementar
        raise NotImplementedError

    def agregar(self, proceso_anonimizacion: ProcesoAnonimizacion):
        proceso_anonimizacion_dto = self._fabrica_anonimizacion.crear_objeto(proceso_anonimizacion, MapeadorProcesoAnonimizacion())
        db.session.add(proceso_anonimizacion_dto)

    def actualizar(self, proceso_anonimizacion: ProcesoAnonimizacion):
        # TODO: Implementar
        raise NotImplementedError

    def eliminar(self, proceso_anonimizacion_id: UUID):
        # TODO: Implementar
        raise NotImplementedError