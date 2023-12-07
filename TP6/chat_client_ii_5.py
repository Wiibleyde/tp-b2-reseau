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
            # Effacer la ligne d'entrée
            print('\b' * len(prompt), end='', flush=True)
            # Afficher le message reçu
            print(response)
            # Réafficher l'invite d'entrée
            print(prompt, end='', flush=True)

    receive_task = asyncio.create_task(receive_messages())

    prompt = "Message : "
    while True:
        message = await aioconsole.ainput(prompt)
        # Effacer la ligne d'entrée
        print('\b' * len(prompt + message), end='', flush=True)
        try:
            await send_message(writer, message)
        except asyncio.CancelledError:
            print("Connexion fermée")
            break
    receive_task.cancel()

if __name__ == '__main__':
    pseudo = input("Pseudo : ")
    asyncio.run(main())