from os import system

def ping(host):
    return system("ping " + host)

if __name__ == "__main__":
    print(ping('8.8.8.8'))