import asyncio
import aioconsole
import argparse

from src.config import Config

global HOST, PORT
HOST = ""
PORT = 0

async def connect_to_server(ip:str, port:int=13337):
    reader, writer = await asyncio.open_connection(ip, port)
    return reader, writer

async def send_message(writer, message):
    writer.write(message.encode())
    await writer.drain()

async def receive_message(reader):
    data = await reader.read(1024)
    return data.decode()

async def main():
    reader, writer = await connect_to_server('127.0.0.1')
    try:
        await send_message(writer, f"Hello|{pseudo}|{room}")
    except asyncio.CancelledError:
        print("Connexion fermée")

    async def receive_messages():
        while True:
            response = await receive_message(reader)
            print('\b' * len(prompt), end='', flush=True)
            print(response)
            print(prompt, end='', flush=True)

    receive_task = asyncio.create_task(receive_messages())

    prompt = "Message : "
    try:
        while True:
            try:
                message = await aioconsole.ainput(prompt)
            except KeyboardInterrupt:
                exit(1)
            print('\b' * len(prompt), end='', flush=True)
            try:
                await send_message(writer, message)
            except asyncio.CancelledError:
                print("Connexion fermée")
                break
    except KeyboardInterrupt:
        print("Déconnexion en cours...")
        writer.close()
        await writer.wait_closed()
        print("Déconnecté.")
        receive_task.cancel()

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-ho", "--host", help="Host IP", type=str, default=config.get_host())
    parser.add_argument("-p", "--port", help="Port", type=int, default=config.get_port())
    return parser.parse_args()

if __name__ == '__main__':
    config = Config("./config_cli.yml")
    args = parse_args() 
    config.set_config(args.host, args.port)
    HOST = config.get_host()
    PORT = config.get_port()
    pseudo = input("Pseudo : ")
    room = input("Room : ")
    asyncio.run(main())