import socket
import sys
import time
import argparse

from src.logs import Logger

def listen(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    try:
        logger.info(f"Un client {addr} s'est connecté.")
        response = conn.recv(1024).decode()
        if response != "":
            logger.info(f"Le client {addr} a envoyé {response}")
            if "meo" in response:
                conn.send("Meo à toi confrère.".encode())
                logger.info(f"Réponse envoyée au client {addr} : Meo à toi confrère.")
            elif "waf" in response:
                conn.send("ptdr t ki".encode())
                logger.info(f"Réponse envoyée au client {addr} : ptdr t ki")
            else:
                conn.send("Mes respects humble humain.".encode())
                logger.info(f"Réponse envoyée au client {addr} : Mes respects humble humain.")
            # sys.stdout.flush()
        return True
    except KeyboardInterrupt:
        conn.close()
        s.close()
        logger.info("Le serveur a été arrêté.")
        exit(0)
    except BrokenPipeError:
        return
    
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

    last_connection_time = time.time()

    while True:
        connection_made = listen('10.1.1.10', args.port)
        logger.debug(f"connection_made = {connection_made}")
        if connection_made:
            last_connection_time = time.time()
        elif time.time() - last_connection_time > 60:
            logger.warning("Aucune connexion n'a été établie depuis plus d'une minute.")
        time.sleep(1)