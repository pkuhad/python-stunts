import time
import thread

def fcn(string, sleeptime, lock, *args):
    while 1:
        lock.acquire()
        print string," Lock Acquired For ", sleeptime
        time.sleep(sleeptime)
        print string," Now releasing Lock"
        lock.release()
        #time.sleep(sleeptime) #Python is not thread safe

if __name__ == "__main__":

    lock = thread.allocate_lock()
    thread.start_new_thread(fcn, ("Thread 1 -", 2, lock))
    thread.start_new_thread(fcn, ("Thread 2 -", 2, lock))
    while 1:
        pass
