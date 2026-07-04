from basic_class import Car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand +"!"
    

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return f"{self.brand} {self.model} with a {self.battery_size} battery"


my_tesla = ElectricCar('Tesla', 'Model S', "85KWh")
print(my_tesla.get_brand())


