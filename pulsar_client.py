import pulsar
from pulsar.schema import *
import uuid
import time

def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ReservaCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('eventos-reserva', subscription_name='my-sub2', schema=AvroSchema(EventoReservaCreada))

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    print("Received value: '%s'" % msg.value())
    print("Received value: '%s'" % msg.value().data)

    consumer.acknowledge(msg)

client.close()