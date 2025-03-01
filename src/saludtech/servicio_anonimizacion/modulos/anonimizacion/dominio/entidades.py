from __future__ import annotations
from dataclasses import dataclass, field

import saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.objetos_valor as ov
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.eventos import ProcesoAnonimizacionCreado, ProcesoAnonimizacionCompletado
from saludtech.servicio_anonimizacion.seedwork.dominio.entidades import AgregacionRaiz, Entidad
import uuid

@dataclass
class ProcesoAnonimizacion(AgregacionRaiz):
    id_proceso_ingestion: uuid.UUID = field(hash=True, default=None)
    imagenes: list[ov.ImagenAnonimizada] = field(default_factory=list[ov.ImagenAnonimizada])
    estado: ov.EstadoAnonimizacion = field(default_factory=ov.EstadoAnonimizacion)
    
    def crear_proceso_anonimizacion(self, proceso_anonimizacion: ProcesoAnonimizacion):
        self.id_proceso_ingestion = proceso_anonimizacion.id_proceso_ingestion
        self.imagenes = proceso_anonimizacion.imagenes
        self.estado = ov.EstadoAnonimizacion(estado="PENDIENTE")

        self.agregar_evento(ProcesoAnonimizacionCreado(
            id_proceso_anonimizacion=self.id, 
            id_proceso_ingestion=self.id_proceso_ingestion, 
            fecha_creacion=self.fecha_creacion
        ))
        
    def completar_anonimizacion(self):
        self.estado = ov.EstadoAnonimizacion(estado="COMPLETADO")
        
        self.agregar_evento(ProcesoAnonimizacionCompletado(
            id_proceso_anonimizacion=self.id,
            id_proceso_ingestion=self.id_proceso_ingestion,
            fecha_actualizacion=self.fecha_actualizacion
        ))