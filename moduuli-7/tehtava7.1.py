def kk():
        kuukaudet = ("talvi" [1], "talvi" [2], "talvi" [3], "kevät" [4], "kevät" [5], "kevät" [6],
                 "kesä" [7], "kesä" [8], "kesä" [9], "syksy" [10], "syksy" [11], "syksy" [12])

kk_str = int(input("Anna kuukauden numero (1-12): "))
if 0< kk_str <4:
    print(f"{kk_str}. kuukausi on talvella.")
if 3< kk_str <7:
    print(f"{kk_str}. kuukausi on keväällä.")
if 6< kk_str <10:
    print(f"{kk_str}. kuukausi on kesällä.")
if 9< kk_str <13:
    print(f"{kk_str}. kuukausi on syksyllä.")

def main():
    print()