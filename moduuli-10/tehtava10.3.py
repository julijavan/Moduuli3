class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi nousi kerrokseen {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi laski kerrokseen {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print(f"Kerros {kerros} ei ole sallittu.")
            return
        print(f"Siirretään hissi kerrokseen {kerros}")
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissin numero")

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"\nHissi {i}:")
            hissi.siirry_kerrokseen(self.alin_kerros)

if __name__ == "__main__":
    talo = Talo(1, 10, 3)

    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 8)
    talo.aja_hissia(2, 3)

    talo.palohälytys()