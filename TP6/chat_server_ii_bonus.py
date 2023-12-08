import asyncio
import time
import random

from src.logs import Logger

global CLIENTS, TERMINAL_COLORS

CLIENTS = {}
TERMINAL_COLORS = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "magenta": "\033[1;35m",
    "cyan": "\033[1;36m",
    "white": "\033[1;37m",
    "reset": "\033[0;0m",
}

async def handle_client(reader, writer) -> None:
    while True:
        data = await reader.read(100)
        addr = writer.get_extra_info('peername')
        if data.decode().startswith("Hello|"):
            pseudo = data.decode().split("|")[1]
            CLIENTS[addr] = {}
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["p"] = pseudo
            CLIENTS[addr]["c"] = chooseRandomColor()
            logger.info(f"Client {addr[0]}:{addr[1]} connected with pseudo {pseudo}")
        elif data:
            message = data.decode()
            for client in CLIENTS:
                logger.info(f"Message from {addr[0]}:{addr[1]} : {message}")
                CLIENTS[client]["w"].write(f"{TERMINAL_COLORS[CLIENTS[addr]['c']]}[{get_time()}] {CLIENTS[addr]['p']} : {message}{TERMINAL_COLORS['reset']}".encode())
                await CLIENTS[client]["w"].drain()
        else:
            logger.info(f"Client {addr!r} disconnected")
            for client in CLIENTS:
                logger.info(f"Client {addr[0]}:{addr[1]} disconnected")
                CLIENTS[client]["w"].write(f"{CLIENTS[addr]['p']} a quitté la chatroom".encode())
                await CLIENTS[client]["w"].drain()
            del CLIENTS[addr]
            break
    logger.info("Close the connection")
    writer.close()

async def main() -> None:
    server = await asyncio.start_server(handle_client, '127.0.0.1', 13337)
    addrs = ', '.join(str(s.getsockname()) for s in server.sockets)
    logger.info(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

def get_time() -> str:
    return time.strftime("%H:%M", time.localtime())

def chooseRandomColor() -> str:
    color = random.choice(list(TERMINAL_COLORS.keys()))
    cpt = 0
    while color == "reset" and cpt < len(TERMINAL_COLORS.keys()):
        color = random.choice(list(TERMINAL_COLORS.keys()))
        cpt += 1
    return color

if __name__ == '__main__':
    logger = Logger()
    logger.info("Lancement du serveur")
    asyncio.run(main())