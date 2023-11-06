import socket
from time import sleep
import regex

def connect(ip, port=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            print(f"Connecté avec succès au serveur {ip} sur le port {port}")
            message = input("Que veux-tu envoyer au serveur : ")
            if type(message) != str:
                raise TypeError("Le message doit être une chaîne de caractères.")
            if regex.match(r"meo|waf", message):
                s.send(message.encode())
                print(s.recv(1024).decode())
            else:
                raise ValueError("Le message doit être obligatoirement 'meo' ou 'waf'.")
    except socket.error:
        print("La connexion a échoué")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

if __name__ == '__main__':
    connect('10.1.1.10')