luvut = []
while True:
    luku = input("Anna luku (tai paina 'enter' lopettaaksesi): ")
    if luku == "":
        break
    try:
        luku = int(luku)
        luvut.append(luku)
    except ValueError:
        print("Luvun tulee olla kokonaisluku.")

suurimmat_viisi = sorted(luvut, reverse=True)[:5]
print("Viisi suurinta lukua: ", suurimmat_viisi)