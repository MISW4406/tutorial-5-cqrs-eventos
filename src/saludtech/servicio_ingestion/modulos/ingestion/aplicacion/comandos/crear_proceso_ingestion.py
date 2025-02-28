from saludtech.servicio_ingestion.seedwork.aplicacion.comandos import Comando
from saludtech.servicio_ingestion.modulos.ingestion.aplicacion.dto import ImagenDTO, ProcesoIngestionDTO
from .base import CrearProcesoIngestionBaseHandler
from dataclasses import dataclass, field
from saludtech.servicio_ingestion.seedwork.aplicacion.comandos import ejecutar_commando as comando
from saludtech.servicio_ingestion.modulos.ingestion.dominio.entidades import ProcesoIngestion
from saludtech.servicio_ingestion.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.servicio_ingestion.modulos.ingestion.aplicacion.mapeadores import MapeadorProcesoIngestion
from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.repositorios import RepositorioProcesoIngestion
import traceback
from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.despachadores import Despachador
@dataclass
class CrearProcesoIngestion(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    imagenes: list[ImagenDTO]
    id_partner: str


class CrearProcesoIngestionHandler (CrearProcesoIngestionBaseHandler):
    
    def handle(self, comando: CrearProcesoIngestion):
        
        proceso_ingestion_dto = ProcesoIngestionDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   imagenes=comando.imagenes,
            id_partner=comando.id_partner)

        proceso_ingestion: ProcesoIngestion = self.fabrica_ingestion.crear_objeto(proceso_ingestion_dto, MapeadorProcesoIngestion())
        proceso_ingestion.crear_proceso_ingestion(proceso_ingestion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoIngestion.__class__)
        try:

            UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, proceso_ingestion)
            UnidadTrabajoPuerto.savepoint()
            UnidadTrabajoPuerto.commit()
        except Exception: 
            print(traceback.format_exc())
            UnidadTrabajoPuerto.rollback()


@comando.register(CrearProcesoIngestion)
def ejecutar_comando_crear_proceso_ingestion(comando: CrearProcesoIngestion):
    handler = CrearProcesoIngestionHandler()
    handler.handle(comando)
    