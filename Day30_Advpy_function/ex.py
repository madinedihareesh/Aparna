'''
iterarator
l=[1,2,3,4] ##any iterable datattype

x=iter(l)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
genarator
print('hello world')
def show():
    return 'Hello word'
print(show())

def mygenarator():
    yield 1
    yield 2
    yield 3

x=mygenarator()

print(next(x))    
print(next(x))    
print(next(x)) 
decorator
clousers+functions with parametrs
'''

def outter(f):
    
    def inner():
        print('+'*10)
        f()
        print('+'*10)
    return inner

@outter ##display=outter(display)
def display():
    print('Hello world')

display()    

   



   


