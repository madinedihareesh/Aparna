'''
Duck typing
class Duck:
    def talk(self):
        print('Duck talks') 
    def walk(self):
        print('Duck walks')

class Dog:
    def talk(self):
        print('Dog Talks')
    def walk(self):
        print('Dog walks')

def person(pet):
    pet.talk()
    pet.walk()

D=Duck()
d=Dog()
person(D)                                           
person(d)
method overloading
l=[1,2,3,4,5]
t=1,2,3,4,5
s={1,2,3,4,5}
d={'one':1,'two':2,'three':3}
s1='python'
print(len(l))
print(len(t))
print(len(s))
print(len(d))
print(len(s1))
method overriding
class A:
    def show(self):
        print('A show method')
class B(A):
    def show(self):
        print('B show Method')

b=A()
b.show()
oparator overloading
print(10+20) ##addition between int
print(12.59+11.23) ##between float
print(2+3j+5+4j) ## complex
print('hello'+'world') ##concantion
'''

# specialization Genralization ##abstraction

                                           
