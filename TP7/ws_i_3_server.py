import asyncio
import websockets

connected = set()

# Chat room server
async def chat_room(websocket, path):
    connected.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            print(message)
            for conn in connected:
                await conn.send(message)
    except websockets.exceptions.ConnectionClosed:
        connected.remove(websocket)

async def main():
    async with websockets.serve(chat_room, "localhost", 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())