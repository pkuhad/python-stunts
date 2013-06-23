import time
import gevent
from gevent import select

'''
The real power of gevent comes when we use it for network and IO bound functions which can be cooperatively scheduled. Gevent has taken care of all the details to ensure that your network libraries will implicitly yield their greenlet contexts whenever possible
'''

start = time.time()
tic = lambda: "at %1.1f seconds" % (time.time() - start)

def gr1():
    print("Started Polling: ", tic())
    select.select([],[],[],2)
    print("Ended Polling: ", tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, at", tic())
    gevent.sleep(1) #Explicit

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr1),
    gevent.spawn(gr3),
])    
