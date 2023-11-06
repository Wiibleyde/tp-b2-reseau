import socket
from time import sleep

def connect(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
    except:
        print("Connection failed")
        return
    try:
        print(f"Connecté avec succès au serveur {ip} sur le port {port}")
        s.send(input("Que veux-tu envoyer au serveur : ").encode())
        print(s.recv(1024).decode())
    except:
        print("Le serveur a fermé la connexion")
        s.close()
        return

if __name__ == '__main__':
    connect('10.1.1.10')
        
