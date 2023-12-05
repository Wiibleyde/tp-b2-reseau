from time import sleep

def compteur():
    for cpt in range(10):
        sleep(0.5)
        print(cpt)
    
if __name__=='__main__':
    compteur()
    compteur()