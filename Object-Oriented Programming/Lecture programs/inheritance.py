# To avoid the repitition we introduce inheritance
# Inheritance is avoiding the common things in programing language.

class Parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
    
class Child1(Parent):
    def __init__(self,name,age,stream):
        super().__init__(name,age)
        self.stream=stream

    def display(self):
        super().display()
        print(self.stream)

class Child2(Parent):
    def __init__(self,name,age,hobby):
        super().__init__(name,age)
        self.hobby=hobby
        
    def display(self):
        super().display()
        print(self.hobby)

child1=Child1('Rohit',19,'Maths')
child1.display()

child2=Child2('Divyanshu',20,'Design')
child2.display()
