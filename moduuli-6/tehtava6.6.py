def laske_yksikkohinta(halk, hinta):
    """
    :Laskee pizzan yksikköhinnan euroina per neliömetri.
    :param halk: Pizzan halkaisija senttimetreinä
    :param hinta: Pizzan hinta euroina
    :return: Yksikköhinta euroina per neliömetri
    """
    sade = halk / 2 / 100  # Muutetaan metreiksi
    pinta_ala = math.pi * (sade ** 2)
    return hinta / pinta_ala

# Pääohjelma
def main():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista:", karsittu_lista)

    halk1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
    halk2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (€): "))

    yksikkohinta1 = laske_yksikkohinta(halk1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halk2, hinta2)

    print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Toinen pizza antaa paremman vastineen rahalle.")