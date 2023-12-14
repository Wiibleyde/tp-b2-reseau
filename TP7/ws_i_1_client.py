import asyncio
import websockets
import aioconsole

async def main(ip: str, port: int):
    async with websockets.connect(f"ws://{ip}:{port}") as websocket:
        while True:
            message = await aioconsole.ainput("Enter message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received {response}")

if __name__ == '__main__':
    asyncio.run(main("localhost", 8765))