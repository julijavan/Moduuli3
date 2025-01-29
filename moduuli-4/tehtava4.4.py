#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

random_luku = random.randint(1, 10)

print("Hei! Arvaa luku väliltä 1..10.")

arvaus = int(input("Arvauksesi: "))

while arvaus != random_luku:
    if arvaus < random_luku:
        print("Liian pieni arvaus.")
    if arvaus > random_luku:
        print("Liian suuri arvaus.")
    arvaus = int(input("Arvauksesi: "))
if arvaus == random_luku:
    print("Vastauksesi on oikein!")