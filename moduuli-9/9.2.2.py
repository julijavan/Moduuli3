class Auto:
    def __init__(self, rtunnus, huippunopeus, current, nopeus, kuljettu):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.current = current
        self.nopeus = []
        self.kuljettu = kuljettu

    def accelerate(self, nopeus):
        self.nopeus.append(30)
        self.nopeus.append(70)
        self.nopeus.append(50)
        self.nopeus.remove(200)

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

        auto = Auto(rtunnus="ABC-123", huippunopeus=142, current=0, nopeus=0, kuljettu=0)
        print(f"Your current speed is {self.nopeus}")