import random


def heita_noppia(lukumäärä):
    summa = 0
    for _ in range(lukumäärä):
        summa += random.randint(1, 6)  # Heitetään yksi noppa (1-6)
    return summa


def main():
    try:
        lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))
        if lukumaara <= 0:
            print("Lukumäärän tulee olla positiivinen kokonaisluku.")
            return

        tulos = heita_noppia(lukumaara)
        print(f"Heittojen summa: {tulos}")
    except ValueError:
        print("Syötteen tulee olla kokonaisluku.")