from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import Comando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.dto import ImagenAnonimizadaDTO, ProcesoAnonimizacionDTO
from .base import AnonimizarProcesoBaseHandler
from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import ejecutar_commando as comando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.entidades import ProcesoAnonimizacion
from saludtech.servicio_anonimizacion.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.mapeadores import MapeadorProcesoAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.repositorios import RepositorioProcesoAnonimizacion
import traceback
import uuid

@dataclass
class AnonimizarProceso(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    imagenes: list[ImagenAnonimizadaDTO]
    id_proceso_original: str

class AnonimizarProcesoHandler(AnonimizarProcesoBaseHandler):
    def handle(self, comando: AnonimizarProceso):
        proceso_anonimizacion_dto = ProcesoAnonimizacionDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            imagenes=comando.imagenes,
            id_proceso_original=comando.id_proceso_original
        )

        proceso_anonimizacion: ProcesoAnonimizacion = self.fabrica_anonimizacion.crear_objeto(
            proceso_anonimizacion_dto, 
            MapeadorProcesoAnonimizacion()
        )
        
        # Realizar la anonimización de los datos
        proceso_anonimizacion.anonimizar_proceso()

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoAnonimizacion.__class__)
        try:
            UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, proceso_anonimizacion)
            UnidadTrabajoPuerto.savepoint()
            UnidadTrabajoPuerto.commit()
        except Exception:
            print(traceback.format_exc())
            UnidadTrabajoPuerto.rollback()

@comando.register(AnonimizarProceso)
def ejecutar_comando_anonimizar_proceso(comando: AnonimizarProceso):
    handler = AnonimizarProcesoHandler()
    handler.handle(comando)