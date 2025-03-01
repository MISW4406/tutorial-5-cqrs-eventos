from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import Comando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.dto import ImagenAnonimizadaDTO, ProcesoAnonimizacionDTO
from .base import ProcesarAnonimizacionBaseHandler
from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import ejecutar_commando as comando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.entidades import ProcesoAnonimizacion
from saludtech.servicio_anonimizacion.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.mapeadores import MapeadorProcesoAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.repositorios import RepositorioProcesoAnonimizacion
import traceback

@dataclass
class ProcesarAnonimizacion(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    imagenes: list[ImagenAnonimizadaDTO]
    id_proceso_ingestion: str
    estado: str


class ProcesarAnonimizacionHandler(ProcesarAnonimizacionBaseHandler):
    
    def handle(self, comando: ProcesarAnonimizacion):
        
        proceso_anonimizacion_dto = ProcesoAnonimizacionDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   imagenes=comando.imagenes
            ,   id_proceso_ingestion=comando.id_proceso_ingestion
            ,   estado=comando.estado)

        proceso_anonimizacion: ProcesoAnonimizacion = self.fabrica_anonimizacion.crear_objeto(proceso_anonimizacion_dto, MapeadorProcesoAnonimizacion())
        proceso_anonimizacion.crear_proceso_anonimizacion(proceso_anonimizacion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProcesoAnonimizacion.__class__)
        try:
            UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, proceso_anonimizacion)
            UnidadTrabajoPuerto.savepoint()
            UnidadTrabajoPuerto.commit()
            
            # Aquí simulamos el proceso de anonimización
            # En un sistema real, este código iría en un worker separado
            for i, imagen in enumerate(proceso_anonimizacion.imagenes):
                # Simular el proceso de anonimización
                proceso_anonimizacion.imagenes[i] = ImagenAnonimizada(
                    tipo=imagen.tipo,
                    archivo=imagen.archivo,
                    archivo_anonimizado=f"anonimizado_{imagen.archivo}"
                )
            
            proceso_anonimizacion.completar_anonimizacion()
            
            UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, proceso_anonimizacion)
            UnidadTrabajoPuerto.commit()
            
        except Exception: 
            print(traceback.format_exc())
            UnidadTrabajoPuerto.rollback()


@comando.register(ProcesarAnonimizacion)
def ejecutar_comando_procesar_anonimizacion(comando: ProcesarAnonimizacion):
    handler = ProcesarAnonimizacionHandler()
    handler.handle(comando)