import gevent
import time
import thread

'''
#Source: http://sdiehl.github.io/gevent-tutorial/#core
The primary pattern used in gevent is the Greenlet, a lightweight coroutine provided to Python as a C extension module. Greenlets all run inside of the OS process for the main program but are scheduled cooperatively.
Only one greenlet is ever running at any given time.
This differs from any of the real parallelism constructs provided by multiprocessing or threading libraries which do spin processes and POSIX threads which are scheduled by the operating system and are truly parallel.

'''

def foo():
    print('Running in foo, I will pass the control after 2 seconds')
    time.sleep(2)
    gevent.sleep(0)
    print("Explicit context switch to foo again")

def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context switch back to bar")

def foo_thread():
    print('Running in foo, I will pass the control after 2 seconds')
    time.sleep(2) #Context switch is being decided by OS. Threads are not useful for CPU Bound tasks, use multiprocessing module.
    print("Done with Foo_thread, but I didn't pass the control after 2 seconds")

def bar_thread():
    print("Running in bar_thread, I want to sleep for 2 seconds")
    time.sleep(2)
    print("Done with Bar_thread")

if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])
    
    thread.start_new_thread(foo_thread,())
    thread.start_new_thread(bar_thread,())
    while 1:
        pass
