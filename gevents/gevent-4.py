import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json

def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']
    print 'Process ', pid, datetime
    return json_result['datetime']


def synch():
    for i in range(1,10):
        fetch(i)

def asynch():
    threads = [gevent.spawn(fetch, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synch()

print('Asynchronous:')
asynch()


