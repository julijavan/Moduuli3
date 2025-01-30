kaupungit = []
for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("Syötetyt kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

    #tai funktiota käyttäen

def main():
    kaupungit = []
    for i in range(5):
        kaupunki = input(f"Anna kaupungin nimi: ")
        kaupungit.append(kaupunki)

    print("Syötetyt kaupungit:")
    for kaupunki in kaupungit:
        print(kaupunki)

    main()