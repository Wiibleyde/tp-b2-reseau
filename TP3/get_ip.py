import psutil

def getIp():
    ips = psutil.net_if_addrs()
    adress = {}
    for i in ips:
        adress[i] = ips[i][0].address
    return adress

if __name__ == "__main__":
    for i in getIp():
        print(i, ":", getIp()[i])
