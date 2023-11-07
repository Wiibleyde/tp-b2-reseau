import socket
import regex

from src.logs import Logger

def connect(ip, port=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            logger.info(f"Connecté réussie à {ip}:{port}")
            message = input("Quel calcul souhaitez vous envoyer ? : ")
            if regex.match(r"^-?([1-9][0-9]{0,4}|100000)$", message):
                s.send(message.encode())
                logger.info(f"Message envoyé au serveur {ip}:{port} : {message}")
                logger.info(f"Réponse du serveur {ip}:{port} : {s.recv(1024).decode()}")
            else:
                raise ValueError("Les nombres doivent être compris entre -100000 et 100000.")
    except socket.error:
        raise ConnectionError(f"Impossible de se connecter au serveur {ip} sur le port {port}")
    except Exception as e:
        logger.critical(f"Une erreur s'est produite: {e}")
        exit(2)

if __name__ == '__main__':
    logger = Logger("./logs/bs_client.log", False)
    connect('10.1.1.10')