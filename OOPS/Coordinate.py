class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def origin_distance(self):
        return self.euclidean_distance(Point(0,0))
    
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
    def point_on_line(line,Point):
        if line.A*Point.x_cod + line.B*Point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lies on the line"
    
         
        
    
    
p1= Point(4,5)
l1= Line(2,4,6)
print(l1)
print(p1) 
print(l1.point_on_line(p1))       