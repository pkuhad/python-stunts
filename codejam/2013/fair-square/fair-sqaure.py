from sys import stdin
import numpy as np
import math

def is_palindrome(number):
    revnumber = str(number)
    revnumber = [item for item in revnumber]
    revnumber.reverse()
    revnumber = ''.join(revnumber)
    #print number
    #print revnumber
    if str(number) == revnumber:
        return True
    else:
        return False

def is_perfect_square(apositiveint):
    if apositiveint == 1:
        return True
    
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    
    return True

def count_fair_and_squre(start, end):
    count = 0
    for number in np.arange(start, end+1):    
        print "checking "+str(number)
        if is_palindrome(number):
            if is_perfect_square(number):
                if is_palindrome(int(math.sqrt(number))):
                    count += 1

    return count

test_cases = int(stdin.next().strip())
for test_case in xrange(1, test_cases+1):
    start, end = map(int, stdin.next().split())
    print "Case #%d: %d" % (test_case, count_fair_and_squre(start, end))


