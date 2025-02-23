import pulsar
from pulsar.schema import *

from saludtech.modulos.ingestion.infraestructura.schema.v1.eventos import EventoProcesoIngestionCreado, ProcesoIngestionCreadoPayload
from saludtech.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearProcesoIngestion, ComandoCrearProcesoIngestionPayload
from saludtech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoProcesoIngestionCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ProcesoIngestionCreadoPayload(
            id_proceso_ingestion=str(evento.id_proceso_ingestion), 
            id_partner=str(evento.id_partner), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoProcesoIngestionCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoProcesoIngestionCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearProcesoIngestionPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearProcesoIngestion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearProcesoIngestion))
