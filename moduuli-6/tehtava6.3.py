def gallona_to_litraa(gallona):
    return gallona * 3.785

def main():
    try:
        while True:
            gallona = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
            if gallona < 0:
                break
            litra = gallona_to_litraa(gallona)
            print(f"{gallona} gallonaa on {litra:.2f} litraa.")
    except ValueError:
            print("Syötteen tulee olla kelvollinen numero.")
main()