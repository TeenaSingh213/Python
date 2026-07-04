class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    



my_car =Car('Toyota', 'Corolla')
print(my_car.brand)
print(my_car.full_name())
class Subjec:
    def __init__(self,name,term):
        self.name=name
        self.term=term
    def marks(self):
        x=int(input("Enter the marks got in mid terms"))
        if self.term=="Mid":
            print("Marks in mid term ",x)
           
            
            
        elif self.term=="End":
           if x<18:
               print("Not eligible for End term exams")
           else:
               print(x*0.4+40, "Marks needed")
op=Subjec("OS","End")
Subjec.marks(op)
# op.marks()