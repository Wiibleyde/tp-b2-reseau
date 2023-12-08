import asyncio

from src.logs import Logger

global CLIENTS
CLIENTS = {}

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        addr = writer.get_extra_info('peername')
        if data.decode().startswith("Hello|"):
            pseudo = data.decode().split("|")[1]
            CLIENTS[addr] = {}
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["p"] = pseudo
            logger.info(f"Client {addr[0]}:{addr[1]} connected with pseudo {pseudo}")
        elif data:
            message = data.decode()
            for client in CLIENTS:
                logger.info(f"Message from {addr[0]}:{addr[1]} : {message}")
                CLIENTS[client]["w"].write(f"{CLIENTS[addr]['p']} : {message}".encode())
                await CLIENTS[client]["w"].drain()
        else:
            print(f"Client {addr!r} disconnected")
            for client in CLIENTS:
                logger.info(f"Client {addr[0]}:{addr[1]} disconnected")
                CLIENTS[client]["w"].write(f"{CLIENTS[addr]['p']} a quitté la chatroom".encode())
                await CLIENTS[client]["w"].drain()
            del CLIENTS[addr]
            break
    logger.info("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 13337)
    addrs = ', '.join(str(s.getsockname()) for s in server.sockets)
    logger.info(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    logger = Logger()
    logger.info("Lancement du serveur")
    asyncio.run(main())