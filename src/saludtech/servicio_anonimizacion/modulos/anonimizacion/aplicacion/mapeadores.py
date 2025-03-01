from saludtech.servicio_anonimizacion.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.servicio_anonimizacion.seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import ProcesoAnonimizacionDTO, ImagenAnonimizadaDTO
from saludtech.servicio_anonimizacion.seedwork.dominio.repositorios import Mapeador
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.objetos_valor import ImagenAnonimizada, EstadoAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.entidades import ProcesoAnonimizacion
from datetime import date


class MapeadorProcesoAnonimizacionDTOJson(AppMap):  

    def externo_a_dto(self, externo: dict) -> ProcesoAnonimizacionDTO:
        proceso_anonimizacion_dto = ProcesoAnonimizacionDTO()
        proceso_anonimizacion_dto.id_proceso_ingestion = externo.get('id_proceso_ingestion')
        proceso_anonimizacion_dto.id = externo.get('id')
        proceso_anonimizacion_dto.fecha_creacion = str(date.today())
        proceso_anonimizacion_dto.estado = externo.get('estado', 'PENDIENTE')
        imagenes: list[ImagenAnonimizadaDTO] = list()
        
        for imagen in externo.get('imagenes', list()):
            imagen_dto: ImagenAnonimizadaDTO = ImagenAnonimizadaDTO(
                imagen.get('tipo'),
                imagen.get('archivo'),
                imagen.get('archivo_anonimizado')
            )
            proceso_anonimizacion_dto.imagenes.append(imagen_dto)

        return proceso_anonimizacion_dto
        
    def dto_a_externo(self, dto: ProcesoAnonimizacionDTO) -> dict:
        return dto.__dict__
        
class MapeadorProcesoAnonimizacion(RepMap):
    def obtener_tipo(self) -> type:
        return ProcesoAnonimizacion.__class__

    def entidad_a_dto(self, entidad: ProcesoAnonimizacion) -> ProcesoAnonimizacionDTO:
        
        proceso_anonimizacion_dto = ProcesoAnonimizacionDTO()
        proceso_anonimizacion_dto.fecha_creacion = entidad.fecha_creacion
        proceso_anonimizacion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        proceso_anonimizacion_dto.id = str(entidad.id)
        proceso_anonimizacion_dto.id_proceso_ingestion = str(entidad.id_proceso_ingestion)
        proceso_anonimizacion_dto.estado = entidad.estado.estado

        imagenes_dto = list()
        
        for imagen in entidad.imagenes:
            imagen_dto = ImagenAnonimizadaDTO()
            imagen_dto.tipo = imagen.tipo
            imagen_dto.archivo = imagen.archivo
            imagen_dto.archivo_anonimizado = imagen.archivo_anonimizado
            imagenes_dto.append(imagen_dto)

        proceso_anonimizacion_dto.imagenes = imagenes_dto

        return proceso_anonimizacion_dto

    def dto_a_entidad(self, dto: ProcesoAnonimizacionDTO) -> ProcesoAnonimizacion:
        proceso_anonimizacion = ProcesoAnonimizacion(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        proceso_anonimizacion.id_proceso_ingestion = dto.id_proceso_ingestion
        proceso_anonimizacion.estado = EstadoAnonimizacion(estado=dto.estado)
        proceso_anonimizacion.imagenes = list()

        imagenes_dto: list[ImagenAnonimizadaDTO] = dto.imagenes
        for imagen_dto in imagenes_dto:
            imagen = ImagenAnonimizada(
                tipo=imagen_dto.tipo,
                archivo=imagen_dto.archivo,
                archivo_anonimizado=imagen_dto.archivo_anonimizado
            )
            proceso_anonimizacion.imagenes.append(imagen)
        
        return proceso_anonimizacion