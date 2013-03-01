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

## Example 1 ##
'''
If a value of variable is dependent on another then nice way to write inline 'if'
'''
b = 11
a = 5 if b>10 else 6

## Example 2 ##
'''
#Source - Learn you a Haskell
Haskell> [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == 24]
So when we are in pythonic mood -
'''
[ (a,b,c) for c in range (1,11) for b in range(1,c) for a in range(1,b) if a+b+c==24 if pow(a,2)+pow(b,2)==pow(c,2)]
#What would happen if 
[ (a,b,c) for c in range (1,11) if c!= 10 for b in range(1,c) for a in range(1,b) if a+b+c==24 if pow(a,2)+pow(b,2)==pow(c,2)]


if __name__ == "__main__":
    print facfunc(3)
    print remove_non_uppercase("adfasdfsADFASDFSdfs")
    print remove_non_uppercase_2("adfasdfsASDFASDFSADF")
    print remove_non_uppercase_2(['a','A'])
