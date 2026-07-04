from basic_class import Car


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
my_tesla=ElectricCar('Tesla', 'Model S'," 85KWh")
print(my_tesla.full_name())

#Aggregation : one class owns the other class
class User:
    def __init__(self):
        self.name = 'nitin'
    
    def login(self):
        print('login')
    
class Student(User):
  
    
    def enroll(self):
        print('enroll into the course')

u=User()
s=Student()
print(s.name)

print(s.login())
print(s.enroll())
        