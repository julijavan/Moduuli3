vuosi = int(input("Anna vuosiluku: "))

#karkausvuodet ovat
if vuosi % 4:
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")
