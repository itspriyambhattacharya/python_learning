class Car:
    # class variable
    total_cars = 0
    # constructor

    def __init__(self, brand, model):
        self.__brand = brand  # changing the acces type of data members from public to private
        self.__model = model  # changing the acces type of data members from public to private
        Car.total_cars += 1

    def display(self):
        return f"{self.__brand} {self.__model}"

    # getter methods
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    # setter methods
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    # polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def display(self):
        return f"{super().display()} and battery size is {self.battery_size}kWh"

    def fuel_type(self):
        return "Electric Charge"


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

c1.set_brand("Hyundai")
c1.set_model("Verna")
print(c1.display())

c3 = ElectricCar("Tesla", "Model1", 4000)
print(c3.display())

# polymorphism test
print(c1.fuel_type())
print(c2.fuel_type())
print(c3.fuel_type())

# print class variable
print(Car.total_cars)
