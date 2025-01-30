import random
import math

# Kysy käyttäjältä pisteiden määrä
while True:
    try:
        points = int(input("Anna arvottavien pisteiden määrä: "))
        if points > 0:
            break
        print("Pisteiden määrän pitää olla positiivinen luku.")
    except ValueError:
        print("Syötä kelvollinen kokonaisluku.")

    # Alustetaan ympyrän sisälle osuneiden pisteiden laskuri
hits = 0

    # Arvotaan pisteitä ja tarkistetaan osuvatko ne ympyrän sisälle
for i in range (points):
    # Arvotaan satunnainen piste neliöstä [-1,1] x [-1,1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Tarkistetaan onko piste yksikköympyrän sisällä
    if x * x + y * y < 1:
        hits += 1

    # Lasketaan piin likiarvo
pii_likiarvo = 4 * hits / points

    # Tulostetaan tulos ja vertailu todelliseen arvoon
print(f"\nPiin likiarvo: {pii_likiarvo}")
print(f"Todellinen pii: {math.pi}")
print(f"Ero todelliseen arvoon: {abs(math.pi - pii_likiarvo)}")