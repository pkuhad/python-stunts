'''
Patterns for syntax best practices
'''

'''
Built in 'itr' function --
>>> i = iter('abc')
>>> i.next()
'a'
>>> i = iter([1,2,3])
>>> i.next
<method-wrapper 'next' of listiterator object at 0x7f8cb6952c90>
>>> i.next()
1
>>> 
'''

class MyIterator(object):
        '''
        Simple class implements 'next' method and '__iter__' which returns an instance of the iterator
        '''

        def __init__(self, step):
                self.step = step

        def next(self):
                '''
                Return the next element. Variable state is checked and if needed then exception is raised to stop the iteration
                '''
                if self.step == 0: # TryIt - What if we don't stop iteration ? Comment if case and stop raising StopIteration, try it.
                        raise StopIteration

                self.step -= 1
                return self.step
        
        def __iter__(self):
                ''' Return the iterator '''
                return self


if __name__ == "__main__":
        
        for el in MyIterator(5):
                print el

        # Enumerating iterations
        for i,el in enumerate(MyIterator(5)):
                print "%d = %d" % (i,el)
