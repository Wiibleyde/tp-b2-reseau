import socket
import sys
from time import sleep

from src.logs import Logger

def connect(ip, port=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")
            message = input("Quel calcul souhaitez vous envoyer ? : ")
            logger.debug(type(message) != str)
            logger.debug(not testIfNumberAreValid(message))
            if type(message) != str or not testIfNumberAreValid(message):
                s.send(message.encode())
                sleep(0.5)
                logger.info(f"Message envoyé au serveur {ip}:{port} : {message}")
                answer = s.recv(1024).decode()
                logger.info(f"Réponse du serveur {ip}:{port} : {answer}")
                print(f"Réponse du serveur {ip}:{port} : {answer}")
                sys.stdout.flush()
            else:
                raise ValueError("Les nombres doivent être compris entre -100000 et 100000 et le calcul doit être de la forme 'nombre1 opérateur nombre2'.")
    except socket.error:
        raise ConnectionError(f"Impossible de se connecter au serveur {ip} sur le port {port}")
    except Exception as e:
        logger.critical(f"Une erreur s'est produite: {e}")
        exit(2)

def testIfNumberAreValid(calcul:int) -> bool:
    nbs = calcul.split(" ")
    if len(nbs) != 3:
        return False
    logger.debug(nbs)
    nbs.pop(1)
    for nb in nbs:
        logger.debug(f"nb: {nb}")
        logger.debug(f"nb.isnumeric(): {nb.isnumeric()}")
        logger.debug(f"{int(nb)} < -100000: {int(nb) < -100000}")
        logger.debug(f"{int(nb)} > 100000: {int(nb) > 100000}")
        if not nb.isnumeric() or not(int(nb) < -100000 or int(nb) > 100000):
            return False
    return True

if __name__ == '__main__':
    logger = Logger("./logs/bs_client.log", False)
    connect('10.1.1.10')