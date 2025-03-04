import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from datetime import datetime

from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.eventos import EventoProcesoAnonimizacionCreado
from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.schema.v1.comandos import ComandoAnonimizarProceso
from saludtech.servicio_anonimizacion.seedwork.infraestructura import utils
from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.comandos.anonimizar_proceso import AnonimizarProceso
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.dto import ImagenAnonimizadaDTO

# Importar el evento de ingestion para escucharlo
from saludtech.servicio_ingestion.modulos.ingestion.infraestructura.schema.v1.eventos import EventoProcesoIngestionCreado

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        
        # Suscribirse a eventos del servicio de ingestion
        consumidor = cliente.subscribe(
            'eventos-proceso_ingestion', 
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='anonimizacion-sub-eventos',
            schema=AvroSchema(EventoProcesoIngestionCreado)
        )

        while True:
            mensaje = consumidor.receive()
            evento_data = mensaje.value().data
            
            print(f'Evento de ingestion recibido para anonimizar: {evento_data}')
            
            # Obtener datos del evento de ingestion para iniciar el proceso de anonimización
            fecha_creacion = datetime.fromtimestamp(evento_data.fecha_creacion / 1000.0).strftime('%Y-%m-%d')
            id_proceso = str(uuid.uuid4())
            
            # Aquí deberíamos obtener las imágenes del proceso original
            # Para simplificar, asumimos un proceso de obtención de imágenes
            imagenes = [
                ImagenAnonimizadaDTO(tipo="imagen", archivo="anonimizado_imagen.jpg", archivo_original="original.jpg")
            ]
            
            # Crear y ejecutar el comando de anonimización
            comando = AnonimizarProceso(
                fecha_creacion=fecha_creacion,
                fecha_actualizacion=fecha_creacion,
                id=id_proceso,
                imagenes=imagenes,
                id_proceso_original=evento_data.id_proceso_ingestion
            )
            
            ejecutar_commando(comando)
            
            # Confirmar recepción del mensaje
            consumidor.acknowledge(mensaje)
            
        cliente.close()
    except Exception as e:
        logging.error(f'ERROR: Suscribiéndose al tópico de eventos! {str(e)}')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'comandos-proceso_anonimizacion', 
            consumer_type=_pulsar.ConsumerType.Shared, 
            subscription_name='anonimizacion-sub-comandos',
            schema=AvroSchema(ComandoAnonimizarProceso)
        )

        while True:
            mensaje = consumidor.receive()
            comando_data = mensaje.value().data
            
            print(f'Comando recibido: {comando_data}')
            
            # Convertir datos de comando a DTO de imágenes
            imagenes = []
            for img_data in comando_data.imagenes:
                imagen_dto = ImagenAnonimizadaDTO(
                    tipo=img_data['tipo'],
                    archivo=img_data['archivo'],
                    archivo_original=img_data.get('archivo_original', '')
                )
                imagenes.append(imagen_dto)
            
            # Crear y ejecutar el comando
            comando = AnonimizarProceso(
                fecha_creacion=comando_data.fecha_creacion,
                fecha_actualizacion=comando_data.fecha_actualizacion,
                id=comando_data.id_proceso_anonimizacion,
                imagenes=imagenes,
                id_proceso_original=comando_data.id_proceso_original
            )
            
            ejecutar_commando(comando)
            
            print("Comando de anonimización ejecutado")
            consumidor.acknowledge(mensaje)
            
        cliente.close()
    except Exception as e:
        logging.error(f'ERROR: Suscribiéndose al tópico de comandos! {str(e)}')
        traceback.print_exc()
        if cliente:
            cliente.close()