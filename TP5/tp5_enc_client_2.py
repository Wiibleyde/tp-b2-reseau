import socket
import sys

from src.logs import Logger

def connect(ip:str, port:int=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")

            message = str(input("Quel calcul souhaitez vous envoyer ? : "))

            if testIfNumberAreValid(message):
                encoded = message.encode(encoding='utf-8')
                splitted = message.split(" ")
                nb1Size, nb2Size, sign = calcNumberSize(int(splitted[0]), int(splitted[2]), splitted[1])
                header = nb1Size.to_bytes(1, 'big') + nb2Size.to_bytes(1, 'big') + sign.to_bytes(1, 'big')
                end = 0
                end = end.to_bytes(1, 'big')
                s.send(header + int(splitted[0]).to_bytes(nb1Size, 'big') + int(splitted[2]).to_bytes(nb2Size, 'big') + end)
                logger.info(f"Message envoyé au serveur {ip}:{port} : {header + int(splitted[0]).to_bytes(nb1Size, 'big') + int(splitted[2]).to_bytes(nb2Size, 'big') + end}")

                positive = s.recv(1) == b'\x01'
                number = int.from_bytes(s.recv(4), 'big')       
                answer = f"{number}" if positive else f"-{number}"
                logger.info(f"Réponse du serveur {ip}:{port} : {answer}")
            else:
                exit(1)
    except socket.error:
        logger.critical(f"Impossible de se connecter à {ip}:{port}")
        exit(1)

def testIfNumberAreValid(calcul:int) -> bool:
    nbs = calcul.split(" ")
    if len(nbs) != 3:
        logger.error(f"Le calcul doit être de la forme 'nombre1 [+ | - | *] nombre2'.")
        return False
    
    if nbs[1] not in ["+", "-", "*"]:
        logger.error(f"Le calcul doit être de la forme 'nombre1 [+ | - | *] nombre2'.")
        return False
    
    try:
        int(nbs[0])
        int(nbs[2])
    except ValueError:
        logger.error(f"Les nombres doivent être des entiers.")
        return False
    
    if int(nbs[0]) > 4294967295 or int(nbs[0]) < 0 or int(nbs[2]) > 4294967295 or int(nbs[2]) < 0:
        logger.error(f"Les nombres doivent être compris entre 0 et 4294967295.")
        return False
    
    return True

def calcMessageSize(message: bytes) -> int:
    return len(message)

def calcNumberSize(nb1:int, nb2:int, sign:str) -> tuple:
    if sign == "+":
        sign = 0
    elif sign == "-":
        sign = 1
    elif sign == "*":
        sign = 2
    nbsList = [nb1, nb2]
    return (len(nbsList[0].to_bytes(4, 'big')), len(nbsList[1].to_bytes(4, 'big')), sign)

if __name__ == '__main__':
    logger = Logger("./logs/bs_client.log", True)
    connect('10.1.1.10')