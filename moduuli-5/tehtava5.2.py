luvut = []
    while True:
        syote = input("Anna luku (tai tyhjä lopettaaksesi): ")
        if syote == "":
            break
        try:
            luku = int(syote)
            luvut.append(luku)
        except ValueError:
            print("Syötteen tulee olla kokonaisluku.")

    suurimmat_viisi = sorted(luvut, reverse=True)[:5]
    print("Viisi suurinta lukua: ", suurimmat_viisi)