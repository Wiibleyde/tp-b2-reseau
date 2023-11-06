import socket
import sys

def listen(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            response = conn.recv(1024).decode()
            print(response.encode())
            sys.stdout.flush()
            if response == 'Meooooo !':
                conn.send("Hi mate !".encode())
        except:
            break
    conn.close()
    s.close()
    
if __name__ == '__main__':
    listen('10.1.1.10')