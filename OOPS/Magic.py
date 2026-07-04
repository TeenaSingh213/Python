class Fraction:
    def __init__(self,x,y):
        
        self.num = x
        self.den = y
    
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

obj = Fraction(3,4)
print(obj)

