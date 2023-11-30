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

            data = conn.recv(1024).decode()
            logger.info(f"Requête reçue du client {addr} : {data}")
            splitted = data.split(" ")
            logger.debug(f"Requête reçue du client {addr} : {splitted}")
            
            if splitted[0] == "GET":
                if splitted[1] == "/":
                    logger.info(f"Envoi de la réponse par défaut au client {addr}.")
                    conn.send("HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>".encode())
                else:
                    try:
                        logger.debug(splitted[1][1:])
                        with open(f"./pages{splitted[1][1:]}", "r") as f:
                            logger.info(f"Envoi du fichier {splitted[1][1:]} au client {addr}.")
                            conn.send("HTTP/1.0 200 OK\n\n".encode() + f.read().encode())
                    except FileNotFoundError:
                        logger.info(f"Envoi de la réponse 404 au client {addr}.")
                        conn.send("HTTP/1.0 404 Not Found\n\n<h1>404 Not Found</h1>".encode())
            else:
                logger.info(f"Envoi de la réponse 404 au client {addr}.")
                conn.send("HTTP/1.0 404 Not Found\n\n<h1>404 Not Found</h1>".encode())
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
