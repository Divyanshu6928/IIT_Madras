class Student:
    count = 0
    def __init__(self,roll_no,name,total) :
        
        self.roll_no=roll_no
        self.name = name
        self.total = total
    
    def display(self):
        print(self.roll_no,self.name)

    def result(self):
        if(self.total > 120):
            print('Conratulations ',self.name ,"you are passed !!")
        else:
            print("Dear",self.name,"Please try again !!") 

s0=Student(0,'Bhuvanesh',100)
s0.result()

s1=Student(1,'Harish',150)
s1.result()

