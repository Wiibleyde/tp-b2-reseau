import asyncio
import time
import random
import argparse

from src.logs import Logger
from src.config import Config

global CLIENTS, TERMINAL_COLORS, ROOMS

ROOMS = {}
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
HOST = ""
PORT = 0

async def handle_client(reader, writer) -> None:
    while True:
        data = await reader.read(100)
        addr = writer.get_extra_info('peername')
        if data.decode().startswith("Hello|"):
            pseudo = data.decode().split("|")[1]
            room = data.decode().split("|")[2]
            CLIENTS[addr] = {}
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["p"] = pseudo
            if room not in ROOMS.keys():
                ROOMS[room] = []
            ROOMS[room].append(addr)
            CLIENTS[addr]["c"] = chooseRandomColor()
            logger.info(f"Client {addr[0]}:{addr[1]} connected with pseudo {pseudo}")
        elif data:
            message = data.decode()
            logger.info(f"Message from {addr[0]}:{addr[1]} : {message}")
            for client in CLIENTS:
                for room in ROOMS:
                    if addr in ROOMS[room] and client in ROOMS[room]:        
                        CLIENTS[client]["w"].write(f"{TERMINAL_COLORS[CLIENTS[addr]['c']]}[{get_time()}] {CLIENTS[addr]['p']} : {message}{TERMINAL_COLORS['reset']}".encode())
                        await CLIENTS[client]["w"].drain()
        else:
            logger.info(f"Client {addr!r} disconnected")
            for client in CLIENTS:
                logger.info(f"Client {addr[0]}:{addr[1]} disconnected")
                for room in ROOMS:
                    if addr in ROOMS[room] and client in ROOMS[room]:
                        CLIENTS[client]["w"].write(f"{TERMINAL_COLORS['red']}[{get_time()}] {CLIENTS[addr]['p']} a quitté la chatroom{TERMINAL_COLORS['reset']}".encode())
                        await CLIENTS[client]["w"].drain()
            del CLIENTS[addr]
            break
    logger.info("Close the connection")
    writer.close()

async def main() -> None:
    server = await asyncio.start_server(handle_client, HOST, PORT)
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
        if color not in [CLIENTS[client]["c"] for client in CLIENTS]:
            break
    return color

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-ho", "--host", help="Host IP", type=str, default=config.get_host())
    parser.add_argument("-p", "--port", help="Port", type=int, default=config.get_port())
    return parser.parse_args()

if __name__ == '__main__':
    config = Config("./config.yml")
    args = parse_args()
    if args.host != config.get_host():
        HOST = args.host
    if args.port != config.get_port():
        PORT = args.port
    logger = Logger("/var/log/chat_room/server.log")
    logger.info("Lancement du serveur")
    asyncio.run(main())