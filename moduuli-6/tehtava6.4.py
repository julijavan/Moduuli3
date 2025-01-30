def summaa_lista(numerot):
    return sum(numerot)
    numerot = [1, 2, 3, 4, 5]
        summa = summaa_lista(numerot)
        print(f"Listan {numerot} summa on {summa}.")
    except ValueError:
        print("Syötteen tulee olla kelvollinen numero.")