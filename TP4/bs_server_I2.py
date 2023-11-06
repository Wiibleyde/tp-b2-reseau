import socket
import sys
from time import sleep

def listen(ip, port=13337):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            print(f"Un client vient de se co et son IP c'est {addr}")
            response = conn.recv(1024).decode()
            if "meo" in response:
                conn.send("Meo à toi confrère.".encode())
            elif "waf" in response:
                conn.send("ptdr t ki".encode())
            else:
                conn.send("Mes respects humble humain.".encode())
            sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except BrokenPipeError:
            break
    conn.close()
    s.close()
    
if __name__ == '__main__':
    while True:
        listen('10.1.1.10')
        sleep(1)