from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.objetos_valor as ov
from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.eventos import ProcesoAnonimizacionCreado
from saludtech.servicio_anonimizacion.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class ProcesoAnonimizacion(AgregacionRaiz):
    id_proceso_original: uuid.UUID = field(hash=True, default=None)
    imagenes: list[ov.ImagenAnonimizada] = field(default_factory=list)
    
    def anonimizar_proceso(self):
        """
        Método principal para iniciar el proceso de anonimización.
        Aplica técnicas de anonimización a los datos/imágenes.
        """
        # Anonimiza cada imagen
        for imagen in self.imagenes:
            imagen.anonimizar()
        
        # Registra el evento de creación del proceso de anonimización
        self.agregar_evento(
            ProcesoAnonimizacionCreado(
                id_proceso_anonimizacion=self.id, 
                id_proceso_original=self.id_proceso_original, 
                fecha_creacion=self.fecha_creacion
            )
        )