# from abc import ABC,abstractmethod
# class Vechical(ABC):
#     def run(self):
#         print('A vehivcal run')

#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vechical):
#     def wheels(self):
#         print('Car has four wheels')
#     def start(self):
#         print('Car starts with key')


# class Bike(Vechical):
#     def wheels(self):
#         print('Bike is having two wheels')

#     def start(self):
#         print('Bike start with kick')    

    
# b=Bike()
# b.start()
# c=Car()
# c.start()
# v=Vechical()
# v.start()
'''
class ATM(ABC):
    def CardlessDiposite(self,amount):
        print('If you are intrested in cardless diposite')
        ac=int(input('Enter your Account NUmber:'))
        otp=int(input('Enter your pin'))
        if ac>0 and otp>0:
            amount=int(input('Enter the amount to diposite: '))
        print('Amount diposited successful')   
    @abstractmethod
    def Checkbal(self):
        pass
    @abstractmethod
    def Diposite(self):
        pass
    @abstractmethod
    def Withdrwal(self):
        pass

class Person(ATM):
    def __init__(self,bal,acc,pin):
        super().__init__()
        self.bal=bal
        self.acc=acc
        self.pin=pin
    def Checkbal(self,pin):
        pin=int(input('Enter you pin))
        if pin==self.pin:
            print(self.bal)
        else:
            print('invalid Pin number')    
    def Diposite(self,disamout):
        self.bal=self.bal+disamout
        print('Diposite successfull your current bal is',self.bal)
    def Withdrwal(self,wamount):
        self.bal=self.bal-wamount
        print(wamount,'withdrwal successfull')
        print('your current account bal is ',self.bal)

p=Person(2000,123,456)
# p.CardlessDiposite(500)   
# p.Checkbal()     
# p.Diposite(500) 
p.Withdrwal(500) 
'''

# class Parent:
#     def display(self):
#         print('parent class')

# class Child(Parent):
#     def show(self):
#         print('Child Class')

# c=Child()
# print(Child.mro())

class Father:
    def dance(self):
        print('the person is a dancer')

class Mother:
    def singer(self):
        print('the person is a singer')

class child(Father,Mother):
    def music(self):
        print('He is a musican')

print(child.mro())


