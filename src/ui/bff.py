import asyncio
import datetime
import random
import websockets
import ssl
import requests


import pulsar
from pulsar.schema import *
from fastavro.schema import load_schema, parse_schema
import uuid
import time
import json

#from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada


async def show_time(websocket):

    json_registry = requests.get('http://localhost:8080/admin/v2/schemas/public/default/eventos-reserva/schema').json()
    json_schema = json.loads(json_registry.get('data',{}))

    schema_definition = parse_schema(json_schema)
    avro_schema = AvroSchema(None, schema_definition=schema_definition)

    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe('eventos-reserva', subscription_name='aeroalpes-bff', schema=avro_schema)
    while True:
        message = json.dumps(consumer.receive().value())
        await websocket.send(message)
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(show_time, "0.0.0.0", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())