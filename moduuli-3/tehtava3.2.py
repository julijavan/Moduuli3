luokka = input("Mikä on hyttiluokkasi? (LUX, A, B, C): ")
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
if luokka != "LUX, A, B, C":
    print("Virheellinen hyttiluokka.")