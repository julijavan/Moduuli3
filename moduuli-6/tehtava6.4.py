def summaa_lista(numerot):
    return sum(numerot)

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

        while True:
            gallona = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
            if gallona < 0:
                break
            litra = gallona_to_litra(gallona)
            print(f"{gallona} gallonaa on {litra:.2f} litraa.")

        numerot = [1, 2, 3, 4, 5]
        summa = summaa_lista(numerot)
        print(f"Listan {numerot} summa on {summa}.")
    except ValueError:
        print("Syötteen tulee olla kelvollinen numero.")