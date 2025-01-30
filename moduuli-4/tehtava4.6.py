import random
import math

while True:
    try:
        points = int(input("Anna arvottavien pisteiden määrä: "))
        if points > 0:
            break
        print("Pisteiden määrän pitää olla positiivinen luku.")
    except ValueError:
        print("Syötä kelvollinen kokonaisluku.")

hits = 0

for i in range (points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        hits += 1

pii_likiarvo = 4 * hits / points

print(f"\nPiin likiarvo: {pii_likiarvo}")
print(f"Todellinen pii: {math.pi}")
print(f"Ero todelliseen arvoon: {abs(math.pi - pii_likiarvo)}")