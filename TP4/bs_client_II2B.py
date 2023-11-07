import socket
import regex

from src.logs import Logger

def connect(ip, port=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")
            message = input("Que veux-tu envoyer au serveur : ")
            if type(message) != str:
                logger.critical("Le message doit être une chaîne de caractères.")
                exit(1)
            if regex.match(r"meo|waf", message):
                s.send(message.encode())
                logger.info(f"Message envoyé au serveur {ip}:{port} : {message}")
                logger.info(f"Réponse du serveur {ip}:{port} : {s.recv(1024).decode()}")
            else:
                raise ValueError("Le message doit être obligatoirement 'meo' ou 'waf'.")
    except socket.error:
        raise f"Impossible de se connecter au serveur {ip} sur le port {port}"
    except Exception as e:
        logger.critical(f"Une erreur s'est produite: {e}")
        exit(2)

if __name__ == '__main__':
    logger = Logger("/var/log/bs_client/bs_client.log", False)
    connect('10.1.1.10')