class Calculate:
    def __init__(self,age):
        self.age=age
    def __add__(self,other) :
        if isinstance (other,Calculate):
            return self.age +other.age
c=Calculate(20) 
c1=Calculate(19)  
print(c+c1)