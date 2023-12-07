import asyncio
import aioconsole

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
        await send_message(writer, f"Hello|{pseudo}")
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
            message = await aioconsole.ainput(prompt)
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

if __name__ == '__main__':
    pseudo = input("Pseudo : ")
    asyncio.run(main())