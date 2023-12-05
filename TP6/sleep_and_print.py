from time import sleep

def compteur():
    for cpt in range(10):
        print(cpt)
        sleep(0.5)
    
if __name__=='__main__':
    compteur()