from saludtech.servicio_anonimizacion.modulos.anonimizacion.dominio.eventos import ProcesoAnonimizacionCreado
from saludtech.servicio_anonimizacion.seedwork.aplicacion.handlers import Handler
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.despachadores import Despachador

class HandlerProcesoAnonimizacionIntegracion(Handler):
    @staticmethod
    def handle_proceso_anonimizacion_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-proceso_anonimizacion')