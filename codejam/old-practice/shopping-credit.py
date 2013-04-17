#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import itertools


if __name__ == "__main__":

    test_cases = raw_input()

    for test_case in xrange(0, int(test_cases)):
        credit_limit = raw_input()
        number_of_items = raw_input()
        items = raw_input()
        
        items = items.split(" ")
        items = [int(item) for item in items]

        for x, item_x in enumerate(items):
            to_compare_with = items[x+1:]
            for y, item_y in enumerate(to_compare_with):
                if (item_x+item_y == int(credit_limit)):
                    output_string = "Case #%d: %d %d " % (test_case+1, x+1, x+y+2)
                    print output_string
                    break
        '''
        solved_list = [list(item) for item in itertools.combinations(items,2) if sum(item)==int(credit_limit)][0]
        output_string = "Case #%d: " % (test_case+1)
        item_index = [items.index(item)+1 for item in solved_list]
        output_string += "%s" % " ".join(str(x) for x in item_index)
        print output_string
        '''

'''
 " ".join([change(item) for item in "%3s" % int(pow((3+math.sqrt(5)), 2)) ])
'''
