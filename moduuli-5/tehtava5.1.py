import random

def roll(amount):
    summa = 0
    for i in range(amount):
        summa += random.randint(1, 6)  # Heitetään yksi noppa (1-6)
    return summa