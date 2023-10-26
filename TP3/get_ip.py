import psutil

if __name__ == "__main__":
    print(psutil.net_if_addrs()['wlp0s20f3'][0][1])
