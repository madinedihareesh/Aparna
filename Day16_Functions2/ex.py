# functions with only opsitional arguments
# we have define '/' to make the before decalred arguments as positional arguments
# def add(a,b,/,c):
#     print(a+b+c)

# add(10,20,c=30)

# functions with keyword only arguments
# def aos(*,s):
#     print('area of squre is',s**2)

# aos(s=5) 


# mixed positonal and key word arguments
# we have to define the positional arguments the we have to keyword argguments
# def mix(a,b,c,/,*,e,f):
#     print(a,b,c,e,f)

# mix(10,20,30,e=40,f=50)

# functions with variable length positonal arguments
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)    

# add(10,20,30,40,50)

# functions with variable length keyword arguments
# def dis(**kwargs):
#     for i in kwargs:
#         print(kwargs[i])

# dis(name='hareesh',age=55)

'''
name='James' ##global variables
# print(name)
def dis():
    name1='sid' ## local variables
    print(name)

dis()
'''
# print(name1)

# function with return statements
# def greet():
#     return 'Hello world','hi there!'


# for i in greet():
#     print(i)


# def math(a,b):
#     sum=a+b
#     mul=a*b
#     sub=a-b
#     return sum,mul,sub

# print(math(20,10))

'''
nested fuctions
clousers
higher order functions
call back functions
recursive function
'''
# nested function calling a function inside another function
# def outter():
#     print('This is the starting of outter function')
    
#     def inner():
#         print('This is inner function')
       
#     print('This is ending of outter function')
#     inner() 

# outter()

# def outter():
#     print('this is the starting of outter function')
#     def inner():
#         print('this is the inner function')
#     print('this is the ending of the outter function')    
#     return inner    
                

# outter()()

# def outter():
#     print('this is the starting of outter function')
#     def inner():
#         print('this is the inner function')
#     print('this is the ending of the outter function')    
#     return inner    
                

# res=outter()
# res()

