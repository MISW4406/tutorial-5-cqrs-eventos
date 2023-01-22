import asyncio
import websockets
import json

from aeroalpes.consumidor import obtener_suscripcion_a_topico

global consumidor

async def procesar_eventos(websocket):

    while True:
        message = json.dumps(consumidor.receive().value())
        await websocket.send(message)
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(show_time, "0.0.0.0", 5678):
        await asyncio.Future()

if __name__ == "__main__":
    consumidor = obtener_suscripcion_a_topico()
    asyncio.run(main())