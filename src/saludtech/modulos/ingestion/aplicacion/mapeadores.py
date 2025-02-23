from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import ProcesoIngestionDTO
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.ingestion.dominio.objetos_valor import Imagen, NombreRegion, Tipo
from saludtech.modulos.ingestion.dominio.entidades import ProcesoIngestion, Region



class MapeadorProcesoIngestionDTOJson(AppMap):  

    def externo_a_dto(self, externo: dict) -> ProcesoIngestionDTO:
        proceso_ingestion_dto = ProcesoIngestionDTO()
        proceso_ingestion_dto.id_partner = externo.get('id_partner')
        
        imagenes: list[ImagenDTO] = list()
        for imagen in externo.get('imagenes', list()):
            imagen_dto: ImagenDTO = ImagenDTO(imagen.get('tipo'),imagen.get('archivo'))
            proceso_ingestion_dto.imagenes.append(imagen_dto)

        return proceso_ingestion_dto
    def dto_a_externo(self, dto: ProcesoIngestionDTO) -> dict:
        return dto.__dict__
class MapeadorProcesoIngestion(RepMap):
    def obtener_tipo(self) -> type:
        return ProcesoIngestion.__class__

    def entidad_a_dto(self, entidad: ProcesoIngestion) -> ProcesoIngestionDTO:
        
        proceso_ingestion_dto = ProcesoIngestionDTO()
        proceso_ingestion_dto.fecha_creacion = entidad.fecha_creacion
        proceso_ingestion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        proceso_ingestion_dto.id = str(entidad.id)

        imagenes_dto = list()
        
        for imagen in entidad.imagenes:
            imagen_dto = ImagenDTO()
            imagen_dto.tipo = imagen.tipo
            imagen_dto.archivo = imagen.archivo
            imagenes_dto.extend(imagen_dto)

        proceso_ingestion_dto.imagenes = imagenes_dto

        return proceso_ingestion_dto

    def dto_a_entidad(self, dto: ProcesoIngestionDTO) -> ProcesoIngestion:
        proceso_ingestion = ProcesoIngestion(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        proceso_ingestion.imagenes = list()

        imagenes_dto: list[ImagenDTO] = dto.imagenes
        for imagen_dto in imagenes_dto:
            tipo= Tipo(imagen_dto.tipo)
            imagen=Imagen(tipo=tipo,archivo=imagen_dto.archivo)
            proceso_ingestion.imagenes.extend(imagen)
        
        return proceso_ingestion