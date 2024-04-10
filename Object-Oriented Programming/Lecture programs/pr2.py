class Student:
    count = 0
    def __init__(self,roll_no,name) :
        
        self.roll_no=roll_no
        self.name = name
    
    def display(self):
        print(self.roll_no,self.name)

s0=Student(0,'Bhuvanesh')
Student.count+=1
s0.display()

s1=Student(1,'Harish')
Student.count+=1
s1.display()

print(Student.count)