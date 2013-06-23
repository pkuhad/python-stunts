import gevent
from gevent import Greenlet

class MyGreenlet(Greenlet):

    def __init__(self, message, name, n):
        Greenlet.__init__(self)
        self.message = message
        self.name = name
        self.n = n
    
    def _run(self):
        print (self.message)
        gevent.sleep(self.n)
        print ("Exiting from ", self.name)

g = MyGreenlet("Hi there", "First", 3)
h = MyGreenlet("Hi there", "Second", 2)
g.start()
h.start()

gevent.joinall([g,h])
