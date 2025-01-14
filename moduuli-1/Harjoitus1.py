nimi = "Juli"
print("Moi " + nimi + ", mitä kuuluu?")
print(f"Moi {nimi}, kuinkas nyt menee?")

# käyttäjän syötteen lukeminen
#huom: input lukee kaikki syötteet
# aina merkkijonoina
lukuA = input("Anna kokonaisluku: ")
#muunnetaan merkkijono kokonaisluvuksi
lukuA = int(lukuA)
# luen käyttäjän suoraan lukuna
lukuB = int( input("Anna toinen luku: "))
summa = lukuA + lukuB

print (f"Lukujesi summa = {summa}")