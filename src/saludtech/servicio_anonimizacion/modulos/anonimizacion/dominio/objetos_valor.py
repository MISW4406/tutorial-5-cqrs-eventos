from __future__ import annotations

from dataclasses import dataclass, field
from saludtech.servicio_anonimizacion.seedwork.dominio.objetos_valor import ObjetoValor
import os
import uuid
import hashlib

@dataclass(frozen=True)
class ImagenAnonimizada(ObjetoValor):
    tipo: str
    archivo: str
    archivo_original: str = ""
    
    def anonimizar(self):
        """
        Método que simula la anonimización de la imagen.
        En una implementación real, aquí se aplicarían técnicas de blur, pixelado, etc.
        Para este ejemplo, simplemente generamos un nuevo nombre de archivo anonimizado.
        """
        # Aquí se implementaría la lógica real de anonimización
        # (por ejemplo, blurring de caras, remoción de metadatos, etc.)
        return self._generar_archivo_anonimizado()
    
    def _generar_archivo_anonimizado(self) -> str:
        """
        Genera un nombre de archivo anonimizado basado en hash del original
        """
        # En una implementación real, aquí se procesaría la imagen
        nombre_base, extension = os.path.splitext(self.archivo)
        hash_obj = hashlib.md5(self.archivo.encode())
        return f"anonimizado_{hash_obj.hexdigest()}{extension}"