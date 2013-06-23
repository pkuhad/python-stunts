import time
from threading import Thread

class MyThread(Thread):

    def __init__(self, bignum):
        Thread.__init__(self)
        self.bignum = bignum

    def run(self):
        for i in range(10):
            for j in range(self.bignum):
                res = 0
                for k in range(self.bignum):
                    res += 1

def test():
    bignum = 1000
    thread = MyThread(bignum)
    thread.start()
    thread.join()

if __name__ == "__main__":
    test()
