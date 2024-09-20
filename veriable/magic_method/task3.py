class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        if isinstance(other,Vector) :
            return self.x + other.x,self.y+other.y
    def __str__(self):
        return f'2d vector {self.x} {self.y}'
v=Vector(3,5)   
v1=Vector(7,9)    
v3=v+v1
print(v3)     