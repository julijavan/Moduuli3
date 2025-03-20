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

    def kuljettu(self, aika):
        self.matka += aika * self.nopeus

autot = []
for i in range(10):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(f'ABC-{i}', huippunopeus))

winnerfound = False

while not winnerfound:
    for auto in autot:
        auto.accelerate(random.randint(-10, 15))
        auto.kuljettu(1)
        if auto.matka >= 10000:
            winnerfound = True

autot.sort(key=lambda a: a.matka)
for auto in autot:
    print(f'{auto.rtunnus}, {auto.huippunopeus}', {auto.nopeus}, {auto.matka})