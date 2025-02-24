import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtech.modulos.ingestion.infraestructura.schema.v1.eventos import EventoProcesoIngestionCreado
from saludtech.modulos.ingestion.infraestructura.schema.v1.comandos import ComandoCrearProcesoIngestion
from aeroalpes.seedwork.infraestructura import utils
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando
def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proceso_ingestion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtech-sub-eventos',schema=AvroSchema(EventoProcesoIngestionCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-proceso_ingestion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-sub-comandos',schema=AvroSchema(ComandoCrearProcesoIngestion))

        while True:
            mensaje = consumidor.receive()
          
            print(mensaje.value().data.id_partner)
            print(f'Comando recibido: {mensaje.value().data}')
            #ejecutar_commando(mensaje.value().data)
            

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()