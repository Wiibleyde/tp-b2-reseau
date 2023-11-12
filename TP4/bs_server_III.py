import socket
import sys
import time
import argparse
from src.logs import Logger

def listen(ip, port=13337, timeout=60):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    s.setblocking(0) 
    logger.info(f"Le serveur tourne sur {ip}:{port}")
    start_time = time.time()
    while True:
        try:
            conn, addr = s.accept()
            logger.info(f"Un client {addr} s'est connecté.")
            response = conn.recv(1024).decode()
            if response != "":
                logger.info(f"Le client {addr} a envoyé {response}")
                answer = str(eval(response))
                conn.send(answer.encode())
                logger.info(f"Réponse envoyée au client {addr} : {answer}")
            conn.close()
            start_time = time.time()
        except socket.error as e:
            if e.errno == 11:
                pass
            else:
                raise
        except KeyboardInterrupt:
            s.close()
            logger.info("Le serveur a été arrêté.")
            exit(0)
        if time.time() - start_time > timeout:
            logger.warning(f"Aucun client depuis plus de {timeout} secondes.")
            start_time = time.time()

def parseArgs():
    parser = argparse.ArgumentParser(description="Serveur de la partie II du TP4")
    parser.add_argument('-p', '--port', type=int, default=13337, help="Port d'écoute du serveur entre 1024 et 65535 (13337 par défaut)")
    return parser.parse_args()

if __name__ == '__main__':
    logger = Logger("/var/log/bs_server/bs_server.log")
    args = parseArgs()
    if args.port < 0 or args.port > 65535:
        if args.port < 1024:
            logger.critical("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
            exit(2)
        else:
            logger.critical("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
            exit(1)
    listen('10.1.1.10', args.port, 60)
