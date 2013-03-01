'''
Concurrency in python
Resources -
http://www.ibm.com/developerworks/aix/library/au-threadingpython/
'''
import threading
import datetime

class ThreadWorker(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" % (self.getName(), now)

for i in range(2):
    t = ThreadWorker()
    t.start()

