import asyncio
import websockets
import redis.asyncio as aioredis

global CLIENT, CONNECTIONS
CONNECTIONS = {}

async def chat_room(websocket, path):
    await add_client(websocket, path)
    try:
        while True:
            message = await websocket.recv()
            print(CONNECTIONS.values())
            for conn in CONNECTIONS.values():
                await conn.send(message)
    except websockets.exceptions.ConnectionClosed:
        await remove_client(websocket)

async def add_client(websocket, path):
    formated_websocket = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"
    await CLIENT.sadd('clients', formated_websocket)
    CONNECTIONS[formated_websocket] = websocket

async def remove_client(websocket):
    formated_websocket = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"
    await CLIENT.srem('clients', formated_websocket)
    del CONNECTIONS[formated_websocket]

async def main():
    async with websockets.serve(chat_room, "localhost", 8765):
        await asyncio.Future()

if __name__ == '__main__':
    CLIENT = aioredis.Redis(host='localhost', port=6379)
    asyncio.run(main())