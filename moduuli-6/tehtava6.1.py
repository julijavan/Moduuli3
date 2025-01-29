import random

def heita_noppa():
    return random.randint(1, 6)

def main():
    while True:
        silmaluku = heita_noppa()
        print(f"Heiton tulos: {silmaluku}")
        if silmaluku == 6:
            break