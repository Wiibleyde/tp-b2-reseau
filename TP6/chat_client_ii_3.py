import asyncio
import aioconsole

async def connect_to_server(ip:str, port:int=13337):
    reader, writer = await asyncio.open_connection(ip, port)
    return reader, writer

async def send_message(writer, message:str):
    writer.write(message.encode())
    await writer.drain()

async def receive_message(reader):
    data = await reader.read(1024)
    return data.decode()

async def main():
    reader, writer = await connect_to_server('127.0.0.1')
    while True:
        message = await aioconsole.ainput("Message : ")
        try:
            await send_message(writer, message)
        except asyncio.CancelledError:
            print("Connexion fermée")
            break
        response = await receive_message(reader)
        print(f"Réponse du serveur : {response}")

if __name__ == '__main__':
    asyncio.run(main())