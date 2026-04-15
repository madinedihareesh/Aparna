from threading import *
from time import *

class Mydata:
    def __init__(self):
        self.data=0
        self.Flag=False
        self.lock=Lock()

    def put(self,d):
        while self.Flag!=False: ##true
            pass
        self.lock.acquire()
        self.data=d
        self.Flag=True
        self.lock.release() 
        sleep(1)   

    def get(self):
        while self.Flag!=True: ##true
            pass
        self.lock.acquire()
        x=self.data
        self.Flag=False
        self.lock.release() 
        sleep(1)
        return x
        
            
def Producer(data):
    i=1
    while True:
        data.put(i)
        print('Producer:',i)
        i+=1 

def Consumer(data):
    while True:
        x=data.get()
        print('consumer: ',x)
data=Mydata()
t1=Thread(target=lambda:Producer(data))
t2=Thread(target=lambda:Consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()