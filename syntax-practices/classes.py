
class testclass():
    attr1 = 'something'
    
    def __init__(self):
        self.attr2 = 'something else'

if __name__ == "__main__":
    '''
    Classes and their instances
    '''
    print testclass.attr1
    #'something'
    instance = testclass
    print instance
    #<class classes.testclass at 0x7f9975ec91f0>
    #No instance is instance -
    instance = testclass()
    print instance
    #<classes.testclass instance at 0x7f9975eea128>
    print instance.attr2
    #'something else'
    print instance.attr1
    #'something'
    instance.attr1 = 'something else else'
    print instance.attr1
    #'something else else'
    print testclass.attr1
    #'something'

    '''
    Meta Programming
    '''
    testclass.attrnew = "Classes are objects itself"
    print instance.attrnew
    testclass.dynamicmethod = lambda self: "I know this about you - %s" % getattr(self, 'attr1')
    print instance.dynamicmethod()

