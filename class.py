# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class with encapsulation
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand, model)  # inherit from Device
        self.__storage = storage  # private attribute

    def install_app(self, app):
        print(f"{app} installed on {self.device_info()}")

    def get_storage(self):
        return f"Storage available: {self.__storage}GB"


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 256)
phone2 = Smartphone("Samsung", "Galaxy S23", 512)

# Use methods
print(phone1.device_info())     # Apple iPhone 14
phone1.install_app("Instagram") # Instagram installed on Apple iPhone 14
print(phone1.get_storage())     # Storage available: 256GB

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
