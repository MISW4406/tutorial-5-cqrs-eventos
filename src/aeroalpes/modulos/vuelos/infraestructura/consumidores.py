import pulsar
from pulsar.schema import *
import uuid
import time

from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva


def suscribirse_a_eventos():
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe('eventos-reserva', subscription_name='aeroalpes-sub', schema=AvroSchema(EventoReservaCreada))

    while True:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        print("Received value: '%s'" % msg.value())
        print("Received value: '%s'" % msg.value().data)

        consumer.acknowledge(msg)
        

    client.close()

def suscribirse_a_comandos():
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe('comandos-reserva', subscription_name='aeroalpes-sub', schema=AvroSchema(ComandoCrearReserva))

    while True:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        print("Received value: '%s'" % msg.value())
        print("Received value: '%s'" % msg.value().data)

        consumer.acknowledge(msg)
        

    client.close()