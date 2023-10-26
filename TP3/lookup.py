from sys import argv
import socket

def lookup(name):
    return socket.gethostbyname(name)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 is_up.py <host>")
        exit(1)
    print(lookup(argv[1]))
