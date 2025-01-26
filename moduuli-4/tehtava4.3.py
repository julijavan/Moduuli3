import math

smallest = math.inf
biggest = -math.inf

number_str = input("Give a number, pressing enter ends the process. :")

while number_str != "":
    luku = float(number_str)

    if luku < smallest:
        smallest = luku
    if luku > biggest:
        biggest = luku

    input("Give another number. ")

print(f"The largest number you entered was {biggest}")
print(f"The smallest number you entered was {smallest}")

