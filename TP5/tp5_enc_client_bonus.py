import socket
import sys

from src.logs import Logger

def connect(ip:str, port:int=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")

            message = str(input("Quel calcul souhaitez vous envoyer ? : "))

            encoded = message.encode(encoding='utf-8')
            
            header = (calcMessageSize(encoded) - 1).to_bytes(2, 'big')
            end = 0
            end = end.to_bytes(1, 'big')
            s.send(header + encoded + end)
            logger.info(f"Message envoyé au serveur {ip}:{port} : {header + encoded + end}")
            positive = s.recv(1) == b'\x01'
            number = int.from_bytes(s.recv(4), 'big')       
            answer = f"{number}" if positive else f"-{number}"
            logger.info(f"Réponse du serveur {ip}:{port} : {answer}")
    except socket.error:
        logger.critical(f"Impossible de se connecter à {ip}:{port}")
        exit(1)

def calcMessageSize(message: bytes) -> int:
    return len(message)

if __name__ == '__main__':
    logger = Logger("./logs/bs_client.log", True)
    connect('10.1.1.10')