'''
Inheritance:
A child can access parent properties and methods

types of inharitence:
1.single Inheritance
class Parent:
    def __init__(self):
        pass
    def display(self):
        print('This is a parent class')

class Child(Parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print('This is a child class')      

c=Child()
c.display() 
c.show()
2.Multiple Inharitance
class Parent1:
    def __init__(self):
        pass
    def display(self):
        print('This is parent1 method')

class Parent2:
    def __init__(self):
        pass
    def show(self):
        print('This is parent2 method')

class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
    def req(self):
        print('This is a child method') 

c=Child()
c.display()
c.show()
c.req()
3.Multi-level Inharitance 
class Grand:
    def __init__(self):
        pass
    def display(self):
        print('This is a Grand class')

class Parent(Grand):
    def __init__(self):
        super().__init__()
    def show(self):
        print('This is a Parent class')

class Child(Parent):
    def __init__(self):
        super().__init__()
    def req(self):
        print('This is a Child class')      

c=Child()
c.display()
c.show()
c.req() 
4.Hirarical Inharitance:
class Parent:
    def __init__(self):
        pass
    def display(self):
        print('This is a Parent class')

class Child1(Parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print('This is a child 1 class')
class Child2(Parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print('This is a child 2 class')

c1=Child1()
c2=Child2()
c1.display()
c1.show() 
c2.display()
c2.show()
5.Hibrid inharitance
class A:
    def __init__(self):
        pass
    def display(self):
        print('This is  class \'A\'')

class B(A):
    def __init__(self):
        super().__init__()
    def show(self):
        print('This is class \'B\'')

class C(A):
    def __init__(self):
        super().__init__()
    def req(self):
        print('This is a class \'C\'') 

class D(B,C):
    def __init__(self):
        super().__init__()

    def res(self):
        print('This is a \'D\'')


d=D()
d.display()
d.req()
d.show()
d.res()



'''







        