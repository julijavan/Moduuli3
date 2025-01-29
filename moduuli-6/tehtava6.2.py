import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

def main():
    try:
        tahkot = int(input("Anna nopan tahkojen määrä: "))
        if tahkot < 1:
            print("Tahkojen määrän tulee olla positiivinen kokonaisluku.")
            return

        while True:
            silmaluku = heita_noppa(tahkot)
            print(f"Heiton tulos: {silmaluku}")
            if silmaluku == tahkot:
                break
    except ValueError:
        print("Syötteen tulee olla kokonaisluku.")