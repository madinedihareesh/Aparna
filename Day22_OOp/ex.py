'''
Object Orineted Programing
class:
class is a blueprint of a object
class is a combination of predefined properties and method
object:
object is an instance of a class
'''
'''
class Name: A class is nothing but a first class functions
   def ___intit__(self):
       variables(properties)
   def m1(self):
       block    
'''

class Sample:
    def __init__(self):
        self.name='AchieversIT'
        self.age=15
    def display(self):
        print(f'The name of Instittue is {self.name} and it started {self.age} ago')  


a=Sample()
b=Sample()
print(a.name)
a.display()
print(b.name)
b.display()


i=10 ## class int
f=12.59 ## class Float
l=[1,2,3,4,5,6] ## class List


class SampleOne:
    # static variables
    a=30
    def __init__(self,name,age):
        self.name=name ##instance variables
        self.age=age
    def show(self):
        print(f'the name{self.name} and age {self.age}')    
    
    @staticmethod   
    def display():
        print(f'hello world')    

mysample=SampleOne('Kiran',40)
print(mysample.name)
print(mysample.age)
print(SampleOne.display())
