import psutil
from os import system
from sys import argv
import socket

def getIp():
    ips = psutil.net_if_addrs()
    adress = {}
    for i in ips:
        adress[i] = ips[i][0].address
    return adress

def ping(host):
    return system("ping -c 1 " + host + " > /dev/null")

def is_up(host):
    if ping(host) == 0:
        return "UP !"
    else:
        return "DOWN !"
    
def lookup(name):
    return socket.gethostbyname(name)
    
if __name__ == "__main__":
    cmd = argv[1]
    if cmd == "ip":
        for i in getIp():
            print(i, ":", getIp()[i])
    elif cmd == "ping":
        print(is_up(argv[2]))
    elif cmd == "lookup":
        print(lookup(argv[2]))
    else:
        print(f"{cmd} is not a valid command. Déso.")