import gevent
import random

def task(pid):
    '''A Non-Deterministic task'''
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task', pid, 'done')

def synch():
    for i in range(1,10):
        task(i)

def asynch():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synch()

print('Asynchronous:')
asynch()

