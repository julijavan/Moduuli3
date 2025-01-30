import random

nopat = int(input("Anna noppien lukumäärä: "))
summa = 0
for i in range(nopat):
    noppa = random.randint(1, 6)
    summa += noppa
print("Silmälukujen summa: ")
print(summa)