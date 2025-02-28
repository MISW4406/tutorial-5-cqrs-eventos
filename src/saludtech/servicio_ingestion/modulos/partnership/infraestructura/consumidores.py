import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
import saludtech.servicio_ingestion.modulos.partnership.infraestructura.consumidores as partnership
from saludtech.servicio_ingestion.seedwork.infraestructura import utils
from saludtech.servicio_ingestion.seedwork.aplicacion.comandos import ejecutar_commando

from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.schema.v1.eventos import EventoProcesoIngestionCreado, ProcesoIngestionCreadoPayload
from saludtech.servicio_ingestion.modulos.partnership.aplicacion.comandos.agregar_proceso_ingestion_partner import AgregarProcesoIngestionPartner 
from saludtech.servicio_ingestion.modulos.partnership.infraestructura.schema.v1.eventos import EventoProcesoIngestionPartnerAgregado

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proceso_ingestion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtech-sub-eventos',schema=AvroSchema(EventoProcesoIngestionCreado))

        while True:
            mensaje = consumidor.receive()
            mc=mensaje.value().data
            timecv= datetime.datetime.fromtimestamp(int(mc.fecha_creacion) / 1000.0, tz=datetime.timezone.utc)
            comando= AgregarProcesoIngestionPartner(id_partner= mc.id_partner,id_proceso_ingestion= mc.id_proceso_ingestion,
            fecha_creacion=str(timecv),fecha_actualizacion= "")
            ejecutar_commando(comando)
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
        consumidor = cliente.subscribe('eventos-proceso_ingestion_partner', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-sub-comandos',schema=AvroSchema(EventoProcesoIngestionPartnerAgregado))

        while True:
            mensaje = consumidor.receive()
    
            print(f'Evento ingestion-partner recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()