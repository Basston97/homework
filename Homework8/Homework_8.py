class Auto:
    def __init__(self, brand, age, mark, color = None, weight = None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    
    def move(self):
        print(f"The {self.brand} {self.mark} is moving.")
    
    def stop(self):
        print(f"The {self.brand} {self.mark} has stopped.")
    
    def birthday(self):
        self.age += 1

class Truck(Auto):
    def __init__(self, max_load):
        super(move).__init__
    
class Car(Auto):
    pass
# Пример использования класса
my_auto = Auto(brand, age, color, mark, weight)
print(f"Brand: {my_auto.brand}")
print(f"Age: {my_auto.age}")
print(f"Color: {my_auto.color}")
print(f"Mark: {my_auto.mark}")
print(f"Weight: {my_auto.weight}")

my_auto.move()
my_auto.stop()

print("Current age:", my_auto.age)
my_auto.birthday()
print("New age after birthday:", my_auto.age)
