import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtech.modulos.partnership.infraestructura.schema.v1.eventos import EventoProcesoIngestionPartnerAgregado
from saludtech.modulos.partnership.infraestructura.schema.v1.comandos import ComandoAgregarProcesoIngestionPartner
from saludtech.seedwork.infraestructura import utils
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando

from saludtech.modulos.ingestion.infraestructura.schema.v1.eventos import EventoProcesoIngestionCreado, ProcesoIngestionCreadoPayload


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proceso_ingestion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtech-sub-eventos')

        while True:
            mensaje = consumidor.receive()
            ejecutar_commando(mensaje.value().data)
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
        consumidor = cliente.subscribe('comandos-proceso_ingestion_partner', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-sub-comandos')

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()