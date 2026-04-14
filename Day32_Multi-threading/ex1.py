from threading import *
from time import *

class Alpha(Thread):
    def run(slef):
        for i in range(65,91):
            print(chr(i))
            sleep(1)
        

t=Alpha()        

t.start()
for i in range(65,91):
    print((i))
    sleep(1)
    
t.join()    