import operator

def facfunc(x):
    '''
    Fun functional way to calculate factorials
    Haskell> product [x,x-1..1] 
    '''
    l = [ item+1 for item in range(0, x) ]
    return reduce(operator.mul, l, 1)

def remove_non_uppercase(st):
    '''
    Take each character ( an element of list in this case ) and apply a predicate
    But hey.. that is the usecase of 'filter', let's get more 'datacentric'
    Haskell> removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]   
    '''
    return "".join([ c for c in st if c.isupper() ])

def myupper(c):
    '''
    As isupper needs an instance
    '''
    return c.isupper()

def remove_non_uppercase_2(stream):
    '''
    Why stream : because -
    #>>> filter(myupper, str)
    #'ALDSJFLJAS' 
    #>>> filter(myupper,['a','A'])
    #['A']
    i.e. string for string and list for list
    '''
    return filter(myupper,stream)

## Example 1
'''
If a value of variable is dependent on another then nice way to write inline 'if'
'''
b = 11
a = 5 if b>10 else 6

##


if __name__ == "__main__":
    print facfunc(3)
    print remove_non_uppercase("adfasdfsADFASDFSdfs")
    print remove_non_uppercase_2("adfasdfsASDFASDFSADF")
    print remove_non_uppercase_2(['a','A'])
