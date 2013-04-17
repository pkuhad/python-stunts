cipher = "zyeqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
decipher = "qaozour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

sort_cipher = list(set([char for char in decipher]))
sort_cipher.sort()
we_have =  "".join(sort_cipher).strip()

assert we_have == "abcdefghijklmnopqrstuvwxyz"

def decode(char):
    return decipher[cipher.index(char)]

def decode_string(string):
    return "".join([decode(char) for char in string])

if __name__== "__main__":
    test_cases = int(raw_input())

    for test_case in xrange(0, test_cases):
        cipher_text = raw_input()
        print "Case #%d: %s" % (test_case+1, decode_string(cipher_text))
