class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # changing the acces type of data members from public to private
        self.__model = model  # changing the acces type of data members from public to private

    def display(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def display(self):
        return f"{super().display()} and battery size is {self.battery_size}kWh"


c1 = Car("Toyota", "Corolla")
c2 = Car("Tata", "Safari")

'''
print(c1.brand)
print(c1.model)
print(c2.model)
'''
print(c1.get_brand())
print(c1.get_model())
print(c2.get_model())
print(c2.display())

c3 = ElectricCar("Tesla", "Model1", 4000)
print(c3.display())
