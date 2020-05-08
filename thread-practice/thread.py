import threading
from threading import Lock
import random
import time
 
sub = 100

lock = Lock()
class th1(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name = threadName)
        print ("starting %s\n" % self.getName()) 
    def run(self):
        dec = 1000
        promo = 20
        while 1:
            global sub
            lock.acquire()
            print ("locking")
            print ("I am %s\n" % self.getName())
            sub = (sub / dec) * promo
            print ("subscriber =",sub)
 
            #tidur selama waktu random
            x = random.randint(1,5)
            time.sleep(x)
            print ("releasing")
            lock.release()

class th2(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name = threadName)
        print ("starting %s\n" % self.getName()) 
    def run(self):
        inflgain = 200
        promo = 10
        while 1:
            global sub
            lock.acquire()
            print ("locking")
            print ("I am %s\n" % self.getName())
            sub = sub + inflgain * promo
            print ("subscriber =",sub)
 
            #tidur selama waktu random
            x = random.randint(1,5)
            time.sleep(x)
            print ("releasing")
            lock.release()


mythread1 = th1("channel1")
mythread2 = th2("channel2")
 
mythread1.start()
mythread2.start()
