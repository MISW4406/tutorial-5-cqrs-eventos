import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.eventos import EventoProcesoAnonimizacionCreado, EventoProcesoAnonimizacionCompletado
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.comandos import ComandoProcesarAnonimizacion
from saludtech.servicio_anonimizacion.seedwork.infraestructura import utils
from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.comandos.procesar_anonimizacion import ProcesarAnonimizacion
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.dto import ImagenAnonimizadaDTO

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proceso_ingestion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='anonimizacion-sub-eventos', schema=AvroSchema(EventoProcesoAnonimizacionCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            
            # Aquí procesaríamos el evento y crearíamos un comando para anonimización
            # Por ejemplo, al recibir un evento de ingestion, iniciaríamos el proceso de anonimización
            
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
        consumidor = cliente.subscribe('comandos-proceso_anonimizacion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='anonimizacion-sub-comandos', schema=AvroSchema(ComandoProcesarAnonimizacion))

        while True:
            mensaje = consumidor.receive()
          
            print(f'Comando recibido: {mensaje.value().data}')
            mc = mensaje.value().data
            
            # Convertir las imágenes del comando a DTOs
            imagenes = []
            for img in mc.imagenes:
                imagen_dto = ImagenAnonimizadaDTO(
                    tipo=img.get('tipo'),
                    archivo=img.get('archivo'),
                    archivo_anonimizado=img.get('archivo_anonimizado')
                )
                imagenes.append(imagen_dto)
            
            comando = ProcesarAnonimizacion(
                fecha_creacion=mc.fecha_creacion,
                fecha_actualizacion=mc.fecha_actualizacion,
                id=mc.id_proceso_anonimizacion,
                id_proceso_ingestion=mc.id_proceso_ingestion,
                imagenes=imagenes,
                estado=mc.estado
            )
            ejecutar_commando(comando)
            
            print("comando ejecutado")
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()