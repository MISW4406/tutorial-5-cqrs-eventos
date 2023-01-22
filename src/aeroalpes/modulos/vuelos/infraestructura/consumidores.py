import pulsar
from pulsar.schema import *
import uuid
import time

from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva
from aeroalpes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    consumidor = cliente.subscribe('eventos-reserva', subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoReservaCreada))

    while True:
        mensaje = consumidor.receive()
        print(f'Evento recibido: {mensaje.value().data}')

        consumidor.acknowledge(mensaje)     

    cliente.close()

def suscribirse_a_comandos():
    cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    consumidor = cliente.subscribe('comandos-reserva', subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoCrearReserva))

    while True:
        mensaje = consumidor.receive()
        print(f'Comando recibido: {mensaje.value().data}')

        consumidor.acknowledge(mensaje)     
        
    cliente.close()