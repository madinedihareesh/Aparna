from threading import *
from time import sleep
def dispaly(string):
    l.acquire()
    for i in string:
        print(i)
        sleep(1)
    l.release()

l=Semaphore(2)

# Lock ##mutex
#Semaphore

t=Thread(target=dispaly,args=('hello world',))   
t1=Thread(target=dispaly,args=('WELCOME',)) 
t2=Thread(target=dispaly,args=('123456789',))

t.start()
t1.start()
t2.start()

t.join()
t1.join()
t2.join()