'''
inner class
class Outter:
    def __init__(self):
        self.name='outter'
        self.inner=self.Inner()
        
    class Inner:
        def __init__(self):
            self.name='inner'

        def greet(self):
            print('Hello World')       

o=Outter()
o.inner.greet() 
class Compeny:
    def __init__(self):
        self.name='TCS'
        self.emp=self.Employee()

    class Employee:
        def __init__(self):
            self.count=1200   
        def saldate(self):
            print('last working of the month')  
c=Compeny()
c.emp.saldate()
Encapsulation:
class En:
    def __init__(self):
        self.name='Capsule'
    def show(self):
        print('En method')


Hiding data: public private(__) protected(_) (data)      

'''
class Bank:
    def __init__(self,bal):
        self.__bal=bal
    def bankname(self):
        print('ICICI')
    def showbal(self):
        print(self.__bal) 
    def get_bal(self):
        print(self.__bal)
    def set_bal(self,amount):
        self.__bal=amount  




class Customer(Bank):
    def __init__(self, bal):
        super().__init__(bal)  

    def custname(self):
        print('Divya')

       

# c=Customer(10000)
# print(c._bal) ## when protected is applicable it dosen't we can not change the data/we should not change the data
# c._bal=200
# print(c._bal)
# # b=Bank(1000)
# # b.showbal()
# # b._Bank__bal=2000 ## name mangling forcebilly connecting
# # b.showbal()
b=Bank(2000)
b.get_bal()
b.set_bal(4000)
b.get_bal()



 


                       