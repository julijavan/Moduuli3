def poista_parittomat(numerot):
    """
    Poistaa annetusta listasta parittomat luvut.
    :param numerot: Lista kokonaislukuja
    :return: Lista, josta on poistettu parittomat luvut
    """
    return [num for num in numerot if num % 2 == 0]


# Pääohjelma
def main():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista:", karsittu_lista)
