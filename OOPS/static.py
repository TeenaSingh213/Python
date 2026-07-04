from basic_class import Car
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        
        

    

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are vehicles that are used for transportation."  # Note: This method is not used in the provided snippets


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric"

    def full_name(self):
        return f"{self.brand} {self.model} with a {self.battery_size} battery"


my_tesla = ElectricCar('Tesla', 'Model S', "85KWh")

print(my_tesla.fuel_type())
safari3= Car('Tata', 'Nexon')
safari=Car('Tata', 'Safari')
safari.model = 'Safari 2023'  # Example of modifying an attribute
print(safari.full_name())  # Example usage of the full_name method
print(safari.fuel_type())
print(safari3.general_description())  # Example usage of the general_description method
def model(self):
    return self.__model  # Example of a method that returns the model attribute