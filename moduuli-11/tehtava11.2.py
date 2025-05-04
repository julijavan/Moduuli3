import random


class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def accelerate(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += aika * self.nopeus


class Sähköauto(Auto):
    def __init__(self, rtunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rtunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def __str__(self):
        return f"Sähköauto {self.rtunnus} (huippunopeus: {self.huippunopeus} km/h, akku: {self.akkukapasiteetti} kWh)"


class Polttomoottoriauto(Auto):
    def __init__(self, rtunnus, huippunopeus, tankin_koko):
        super().__init__(rtunnus, huippunopeus)
        self.tankin_koko = tankin_koko

    def __str__(self):
        return f"Polttomoottoriauto {self.rtunnus} (huippunopeus: {self.huippunopeus} km/h, tankki: {self.tankin_koko} l)"


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autolista
        self.tunnit = 0

    def tunti_kuluu(self):
        self.tunnit += 1
        for auto in self.autot:
            auto.accelerate(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}: {self.tunnit} tuntia ajettu")
        print(f"{'Rekisteritunnus':<15}{'Huippunopeus':<15}{'Nopeus':<15}{'Kuljettu matka':<15}{'Maalissa':<10}")
        print("-" * 70)

        jarjestetyt_autot = sorted(self.autot, key=lambda a: a.matka, reverse=True)

        for auto in jarjestetyt_autot:
            maalissa = "KYLLÄ" if auto.matka >= self.pituus else "EI"
            print(f"{auto.rtunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<15}{auto.matka:<15.1f}{maalissa:<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

def kilpailu_main():
    # Luodaan autolista
    autot = []
    for i in range(10):
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(f'ABC-{i + 1}', huippunopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()

        if kilpailu.tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    print("\nKILPAILU PÄÄTTYNYT!")
    kilpailu.tulosta_tilanne()

    # Etsitään voittaja
    voittaja = max(kilpailu.autot, key=lambda a: a.matka)
    print(f"\nKilpailun '{kilpailu.nimi}' voitti auto {voittaja.rtunnus}")
    print(f"Voittajan tiedot: Huippunopeus: {voittaja.huippunopeus} km/h, Loppunopeus: {voittaja.nopeus} km/h")
    print(f"Kilpailun kesto: {kilpailu.tunnit} tuntia")


def main():
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    print("Autot:")
    print(sahkoauto)
    print(polttomoottoriauto)
    print()

    sahkoauto.accelerate(120)
    polttomoottoriauto.accelerate(100)

    print("Autojen nopeudet:")
    print(f"{sahkoauto.rtunnus}: nopeus {sahkoauto.nopeus} km/h")
    print(f"{polttomoottoriauto.rtunnus}: nopeus {polttomoottoriauto.nopeus} km/h")
    print()

    ajoaika = 3
    sahkoauto.kulje(ajoaika)
    polttomoottoriauto.kulje(ajoaika)

    print(f"Ajon jälkeen ({ajoaika} tuntia):")
    print(f"{sahkoauto.rtunnus}: kuljettu matka {sahkoauto.matka:.1f} km")
    print(f"{polttomoottoriauto.rtunnus}: kuljettu matka {polttomoottoriauto.matka:.1f} km")


if __name__ == "__main__":
    main()