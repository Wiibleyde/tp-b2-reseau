import socket

def listen(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        if conn.recv(1024).decode() == 'Meooooo !':
            conn.send("Hi mate !".encode())

if __name__ == '__main__':
    listen('10.1.1.10')