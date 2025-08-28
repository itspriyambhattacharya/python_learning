class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def display(self):
        return f"{super().display()} and battery size is {self.battery_size}kWh"


c1 = Car("Toyota", "Corolla")
c2 = Car("Tata", "Safari")

print(c1.brand)
print(c1.model)
print(c2.model)
print(c2.display())

c3 = ElectricCar("Tesla", "Model1", "4000")
print(c3.display())
