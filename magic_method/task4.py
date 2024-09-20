class vector:
    def __init__(self,x,y):
        self.x=y
        self.y=y
    def __add__(self,other):
        if isinstance(other,vector) :
            return self.x+other.x, self.y+other.y
    def __lt__(self,other):
        if isinstance(other,vector):
            return self.magnitude_square () < other.magnitude_square()
    def __eq__(self,other):
        if isinstance(other,vector):
            return self.x==other.x,self.y==other.y
    def magnitude_square(self):
        return self.x **2 +self.y**2
    def __str__(self) :
        return self.x + self.y 
v=vector(5,5)   
v1=vector(10,10)         
v2=vector(5,20)
v4=v+v1
print(v4)
              
print(v<v1)
print(v==v2)