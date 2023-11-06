import socket 

def connect(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send("Meooooo !".encode())
    print(s.recv(1024).decode())
    s.close()

if __name__ == '__main__':
    connect('10.1.1.10')
