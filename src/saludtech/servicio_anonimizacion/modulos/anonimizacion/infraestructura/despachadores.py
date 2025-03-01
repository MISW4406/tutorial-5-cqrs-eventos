import pulsar
from pulsar.schema import *

from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.eventos import EventoProcesoAnonimizacionCreado, ProcesoAnonimizacionCreadoPayload, EventoProcesoAnonimizacionCompletado, ProcesoAnonimizacionCompletadoPayload
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.comandos import ComandoProcesarAnonimizacion, ComandoProcesarAnonimizacionPayload
from saludtech.servicio_anonimizacion.seedwork.infraestructura import utils

from datetime import datetime

epoch = datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        if topico == "eventos-proceso_anonimizacion":
            payload = ProcesoAnonimizacionCreadoPayload(
                id_proceso_anonimizacion=str(evento.id_proceso_anonimizacion), 
                id_proceso_ingestion=str(evento.id_proceso_ingestion), 
                fecha_creacion=int(datetime.strptime(evento.fecha_creacion, '%Y-%m-%d').timestamp() * 1000)
            )
            evento_integracion = EventoProcesoAnonimizacionCreado(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoProcesoAnonimizacionCreado))
        
        elif topico == "eventos-proceso_anonimizacion_completado":
            payload = ProcesoAnonimizacionCompletadoPayload(
                id_proceso_anonimizacion=str(evento.id_proceso_anonimizacion), 
                id_proceso_ingestion=str(evento.id_proceso_ingestion), 
                fecha_actualizacion=int(datetime.strptime(evento.fecha_actualizacion, '%Y-%m-%d').timestamp() * 1000)
            )
            evento_integracion = EventoProcesoAnonimizacionCompletado(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoProcesoAnonimizacionCompletado))

    def publicar_comando(self, comando, topico):
        imagenes = list()
        for imagen in comando.imagenes:
            imagenes.append({
                "tipo": imagen.tipo, 
                "archivo": imagen.archivo,
                "archivo_anonimizado": imagen.archivo_anonimizado
            })
        
        payload = ComandoProcesarAnonimizacionPayload(
            id_proceso_ingestion=str(comando.id_proceso_ingestion),
            fecha_creacion=str(comando.fecha_creacion),
            fecha_actualizacion=str(comando.fecha_actualizacion),
            id_proceso_anonimizacion=str(comando.id),
            imagenes=imagenes,
            estado=comando.estado
        )
       
        comando_integracion = ComandoProcesarAnonimizacion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoProcesarAnonimizacion))