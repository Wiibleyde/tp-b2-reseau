import socket

def connect(ip, port=13337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            print(f"Connecté avec succès au serveur {ip} sur le port {port}")
            s.send(input("Que veux-tu envoyer au serveur : ").encode())
            print(s.recv(1024).decode())
    except socket.error:
        print("La connexion a échoué")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

if __name__ == '__main__':
    connect('10.1.1.10')