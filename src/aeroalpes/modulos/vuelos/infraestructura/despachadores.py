import pulsar
from pulsar.schema import *

from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada, ReservaCreadaPayload


import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despechador:
    def publicar(self, evento):
        client = pulsar.Client('pulsar://localhost:6650')

        producer = client.create_producer('eventos-reserva', schema=AvroSchema(EventoReservaCreada))

        payload = ReservaCreadaPayload(id_reserva=str(evento.id_reserva), 
        id_cliente=str(evento.id_cliente), 
        estado=str(evento.estado), 
        fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )

        evento_integracion = EventoReservaCreada(data=payload)

        producer.send(evento_integracion)

        client.close()