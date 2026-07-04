class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person("teena",'female')
p2 = Person('abhay','male')

l=[p1,p2]
d1 = {'p1': p1, 'p2':p2}

for i in l:
    print(i.name,i.gender)
    
for i in d1:
    print(d1[i].name)
    