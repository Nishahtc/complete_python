class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(Person) :
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id=student_id
    def display_info(self):
        print(f"person name {self.name} and age is {self.age} now adding student id {self.student_id}") 
s=student("nisha",19,1)    
print(s.display_info())  
  
