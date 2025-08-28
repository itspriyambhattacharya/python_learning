class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def get_brand(self):
        return self.__brand

    @property
    def get_model(self):
        return self.__model

    @get_model.setter
    def set_model(self, model):
        self.__model = model

    def display(self):
        return f"{self.__brand} {self.__model}"


# test
c1 = Car("Brand 1", "Model 1")
c2 = Car("Brand 2", "Model 1")
print(c1.get_brand)
print(c1.display())
print(c2.display())

# modify

c1.set_model = "Updated Model"
print(c1.display())
