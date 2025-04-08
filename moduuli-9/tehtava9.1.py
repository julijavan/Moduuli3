class Car:
    def __init__(self, rektunnus, top_speed, kuljettu):
        self.rektunnus = rektunnus
        self.top_speed = top_speed
        self.kuljettu = kuljettu

car1 = Car("ABC-123", 142, 0)
print(f"Your car's plate number is {car1.rektunnus}.")
print(f"Your car's top speed is {car1.top_speed}.")
print(f"Your car's mileage is {car1.kuljettu}.")