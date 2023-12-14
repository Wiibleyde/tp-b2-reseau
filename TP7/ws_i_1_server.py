import asyncio
import websockets

async def serve(websocket):
    message = await websocket.recv()
    print(f"Received {message}")
    await websocket.send(f"Hello client ! Received {message}")

    
async def main():
    async with websockets.serve(serve, "localhost", 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
