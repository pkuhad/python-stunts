from sys import stdin
import numpy as np

notation = {
    'player' : 'X',
    'enemy'  : 'O',
    'friend' : 'T',
    'empty'  : '.',
    }    

def check_for_win(tic_tac):
    for row in range(0,4):
        result = check_list_for_win(tic_tac[row])
        if result['win']:
            return result

    for col in range(0,4):
        result = check_list_for_win(tic_tac[:,col])
        if result['win']:
            return result


    result = check_list_for_win(tic_tac.diagonal(0,1,0))
    if result['win']:
        return result 
        

    result = check_list_for_win(np.fliplr(tic_tac).diagonal(0,1,0))
    if result['win']:
        return result

    return {'win': False}

def check_for_empty(tic_tac):
    return np.argwhere(tic_tac==notation['empty']).size

def check_list_for_win(array):
    win = True
    winner = ''
    for item in range(0,4):
        if array[item] == notation['empty']:
            win = False
        elif array[0] == array[item] or array[item] == notation['friend']:
            if not winner and ( not array[item] == notation['empty'] ):
                winner = array[item]
            pass
        else:
            win = False

    return {'winner': winner, 'win': win} 


test_cases = int(stdin.next().strip())
for test_case in xrange(1, test_cases+1):
    tic_tac = np.array(np.arange(16).reshape(4,4), dtype=object)
    for i in range(0,4):
        string = stdin.next().split()[0]
        tic_tac[i] = [char for char in string]
    result = check_for_win(tic_tac)
    if result['win']:
        print "Case #%d: %s won" % (test_case, result['winner'])
    elif check_for_empty(tic_tac):
        print "Case #%d: Game has not completed" % test_case
    else:
        print "Case #%d: Draw" % test_case
    try:
        stdin.next()
    except StopIteration:
        pass

