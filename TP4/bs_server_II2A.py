import socket
import sys
from time import sleep
import argparse

from src.logs import Logger

def listen(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            print(f"Un client vient de se co et son IP c'est {addr}")
            response = conn.recv(1024).decode()
            if "meo" in response:
                conn.send("Meo à toi confrère.".encode())
            elif "waf" in response:
                conn.send("ptdr t ki".encode())
            else:
                conn.send("Mes respects humble humain.".encode())
            sys.stdout.flush()
        except KeyboardInterrupt:
            conn.close()
            s.close()
        except BrokenPipeError:
            break
    
def parseArgs():
    parser = argparse.ArgumentParser(description="Serveur de la partie II du TP4")
    parser.add_argument('-p', '--port', type=int, default=13337, help="Port d'écoute du serveur entre 1024 et 65535 (13337 par défaut)")
    return parser.parse_args()

if __name__ == '__main__':
    logger = Logger("/var/log/bs_server/bs_server.log")
    args = parseArgs()
    if args.port < 0 or args.port > 65535:
        if args.port < 1024:
            logger.critical("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
            exit(2)
        else:
            logger.critical("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
            exit(1)
    logger.info(f"Le serveur tourne sur localhost:{args.port}")
    while True:
        listen('localhost', args.port)
        sleep(1)