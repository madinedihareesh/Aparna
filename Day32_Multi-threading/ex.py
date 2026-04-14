from threading import *
from time import *

def display():
    for i in range(65,91):
        print(chr(i))
        

t=Thread(target=display,name='Alpha')        

t.start()
for i in range(65,91):
    print((i))
    
t.join()    