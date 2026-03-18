'''
function:
predifined block of resuable code when we required
'''
'''
def Functionname(parameters/arguments): formal arguments
    block of code

calling a function:
Functionname(parametrs/arguments) actual arguments    
'''
# functions without parametrs/arguments
def geetings():
    print('Hello world')

geetings()

# function with arguments
def geet(name):
    print(f'hello {name}')

geet('Divya') 

'''
fucntion two types:
predefined(built in function)(print(),enumnarate(),del(),len(),zip())
userdefined function()
'''
def prime(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i+=1    
    if count==2:
        print(a,'is a prime number')
    else:
        print(a,'is not a prime number')    

num=int(input('Enter the number:'))
prime(num)
prime(18)

# function default parametrs:
# def add(a,b,c):
#     print(a,b,c)

# add(b=10,a=20,c=30)





