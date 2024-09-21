class Student_data:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def display_info(self):
        return f'student name is {self.name} and student age is {self.age},\n'    
s=Student_data("nisha",19)
print(getattr(s,"age"))
print(setattr(s,"name","nishu"))
delattr(s,"age")
print(s.display_info())