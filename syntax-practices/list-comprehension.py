'''
Patterns for syntax best practices
'''

def _format_string(pos, element):
        return "%d: %s" % (pos, element)

def demo_list_comprehension():
        
        ## Simple list comprehension ##
        li = [i for i in range(10) if i % 2 == 0]
        #print li

        ## Enumeration ##
        seq = ["one", "two", "three"]

        # Remember that this is an ordered list
        # for i in range(3):
        #        print seq[i]
        
        # Now we 'enumerate'
        for i,element in enumerate(seq):
                seq[i] = "%d: %s" % (i, seq[i]) # New value = fn( Current value )

        #print seq

        # Using list comprehension again
        seq = ["one", "two", "three"]
        print [_format_string(i, el) for i,el in enumerate(seq)]
        print [_format_string(i, el) for i,el in enumerate(range(10)) if ( el % 2 == 0 )]


if __name__ == "__main__":
        demo_list_comprehension()

