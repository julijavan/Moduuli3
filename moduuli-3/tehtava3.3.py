#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Anna biologinen sukupuolesi (mies/nainen): ")

if sukupuoli not in ["mies", "nainen"]:
    print("Anna joko 'mies' tai 'nainen'. Anteeksi kun yleistämme.")
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen" and hemoglobiini <=117:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "nainen" and 117<=hemoglobiini<=175:
    print("Hemoglobiini on normaali.")
if sukupuoli == "nainen" and hemoglobiini >=175:
    print("Hemoglobiini on korkea.")

if sukupuoli == "mies" and hemoglobiini <=134:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "mies" and 134<=hemoglobiini<=195:
    print("Hemoglobiini on normaali.")
if sukupuoli == "mies" and hemoglobiini >=195:
    print("Hemoglobiini on korkea.")
