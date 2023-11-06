import socket
from time import sleep

def connect(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
    except:
        print("Connection failed")
        return
    print(f"Connecté avec succès au serveur {ip} sur le port {port}")
    s.send(input("Que veux-tu envoyer au serveur : ").encode())
    print(s.recv(1024).decode())
    s.close()

if __name__ == '__main__':
    while True:
        connect('10.1.1.10')
        sleep(1)
        
