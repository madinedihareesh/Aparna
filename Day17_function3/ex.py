# Advance function
# clousers
'''
if the inner function is having the abiluty
to read the outter function variables then 
the function is know as clouser
'''
'''
def outter():
    name='James'
    def inner():
        print(name)
    inner()
outter()  
def outter(name):
    def inner():
        print(name)
    inner()
outter('james') 
'''             
# higer order function
'''
if a function is having a ability to read
the other function as a parameter
then that function is know as higer order function
'''
'''
def sample():
    print('Hello world')
    

def greet(a): ##greet is a higher order function
    print('+'*10)
    a() ##sample() is a call-back function
    print('+'*10)
greet(sample)     
'''
       
# call back function
'''
if a function can pass as a arrgument to
another then that function is known as ]
call back function
'''
# recersive function
# factoral 5! 
'''
def fact(a):
    if a<=0:
        return 1
    else:
        return a*fact(a-1)
    
print(fact(5))  
''' 
# lamda function(map(),filter())
'''
lambda function is also know as anonomus function

lambda value:expression
'''
# squre=lambda x:x**2
# print(squre(5))
# add=lambda a,b:a+b
# print(add(10,20))


# map()
# filter()
l=[1,2,3,4,5,6,7,8,9,10]
f=list(filter(lambda x:x%2==0,l))
print(f)

l1=['1','2','3','4']
m=list(map(lambda x:int(x),l1))
print(m)

def add(a,b,c):
    return a+b+c

l2=[10,20,30]
l3=[1,2,3]
l4=[4,5,6]

res=map(add,l2,l3,l4)
print(list(res))
