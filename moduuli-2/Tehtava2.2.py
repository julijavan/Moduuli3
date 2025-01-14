import math

sade_str = float(input("Mika on ympyrän sade? "))
# ilmoitettu säde potenssiin kaksi, kertaa 3,14
pintal = math.pi * int(sade_str ** 2)
print(pintal)