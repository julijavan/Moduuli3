def gallona_to_litra(gallona):
    return gallona * 3.785

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
    except ValueError:
        print("Syötteen tulee olla kelvollinen numero.")