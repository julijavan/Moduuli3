class Auto:
    def __init__(self, rektunnus, huippunopeus, nopeus, current, kuljettu):
        self.rekunnus = rektunnus
        self.huippunopeus = huippunopeus
        self.current = current
        self.kuljettu = kuljettu
        self.nopeus = nopeus

    def accelerate(self, nopeus):
        self.nopeus.append(30)
        self.nopeus.append(70)
        self.nopeus.append(50)

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

auto1 = Auto(rektunnus="ABC-123", huippunopeus=142, current=0, nopeus=0, kuljettu=0)
print(f"Your current speed is {auto1.nopeus}")