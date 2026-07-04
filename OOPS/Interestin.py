class Person:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(person):
    print('hi myself',person.name,'and I am a',person.gender)
    p1=Person('Abhay','Male')
    return p1

p = Person('Teena','Female')
print(greet(p))
x = greet(p)
print(x.name)
print(x.gender)