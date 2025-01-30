onAlku = True

luku = int(input("Anna kokonaisluku: "))

#jos annettu luku on jaollinen yhdelläkin
#muuttujan jakaja arvollam niin luku EI ole alkuluku

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        onAlku = False
        #nyt tiedetään jo lopputulos,
        #for-toisto voidaan lopettaa heti
        break

if onAlku:
    print("Lukusi ON alkuluku!")
else:
    print("Lukusi EI ole alkuluku!")