def poista_parittomat(numerot):
    return [num for num in numerot if num % 2 == 0]


# Pääohjelma
def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista_parittomat(lista)

    print("Alkuperäinen lista:", lista)
    print("Karsittu lista:", karsittu_lista)

main()
