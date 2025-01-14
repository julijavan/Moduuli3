gram = 1
bullet = gram * 13.3
nail = bullet * 32
leiviska = nail * 20

L2_str = float(input("Montako leiviskaa? "))
N2_str = float(input("Montako naulaa? "))
B2_str = float(input("How many bullets? "))

massG = (int(L2_str * leiviska) + int(N2_str * nail) + int(B2_str * bullet))
massKG = massG / 1000
massGG = massG%1000
print(f"Paino nykyaikana {massKG} kg ja {massGG} g.")