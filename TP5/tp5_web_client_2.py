import socket
import sys

from src.logs import Logger

def connect(ip:str, port:int=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")

            s.send(b"GET /")
            logger.info(f"Message envoyé au serveur")

            answer = s.recv(1024).decode()
            logger.info(f"Réponse du serveur {ip}:{port} : {answer}")
    except socket.error:
        logger.critical(f"Impossible de se connecter à {ip}:{port}")
        exit(1)

if __name__ == '__main__':
    logger = Logger("./logs/bs_client.log", True)
    connect('10.1.1.10')