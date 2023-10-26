from os import system
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 is_up.py <host>")
        exit(1)
    print(system(f"ping {argv[1]}"))