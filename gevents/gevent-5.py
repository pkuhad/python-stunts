import time

def echo(i):
    time.sleep(0.001)
    return i

from multiprocessing.pool import Pool
p = Pool(10)

print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]

# ^ Is this distribution random ?

from gevent.pool import Pool

p = Pool(10)

print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]
print [a for a in p.imap_unordered(echo, xrange(10))]

