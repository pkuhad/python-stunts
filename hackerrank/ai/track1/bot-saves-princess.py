#!/bin/python
# Head ends here

# Solving - https://www.hackerrank.com/categories/ai/introduction

X = 0
Y = 1


class mybot():

    def __init__(self, n, grid):
        self.n = n
        self.grid = grid

        self.q = []
        self.current = self._get_my_position()
        self.current_track = None
        self.q.append([self.current])
        self.visited = [self.current]

    def test_things(self):
        self.current_track = [(1,1),(1,0),(2,0)]
        return self._got_queen()

    def find_move(self):
        steps = self._find_move()
        self._parse_steps(steps)
    
    def _find_move(self):

        while 1:
            self.current_track = self.q.pop() # Assumption that there is an element in q
            if self._got_queen():
                return self.current_track

            for move in [self._get_left_move(), self._get_right_move(), self._get_up_move(), self._get_down_move()]:
                if(self._is_valid_move(move)):
                    new_current_track = list(self.current_track)
                    new_current_track.append(move)
                    self.visited.append(move)
                    self.q.append(new_current_track)
    
    def _get_left_move(self):
        return (self.current_track[-1][X], self.current_track[-1][Y]-1)
    
    def _get_right_move(self):
        return (self.current_track[-1][X], self.current_track[-1][Y]+1)
    
    def _get_up_move(self):
        return (self.current_track[-1][X]-1, self.current_track[-1][Y])
    
    def _get_down_move(self):
        return (self.current_track[-1][X]+1, self.current_track[-1][Y])

    def _is_valid_move(self, move):
        if( move[X]<0 or move[Y]<0 or move[X]>=self.n or move[Y]>= self.n ):
            return False;
        if ( (move[X],move[Y]) in self.visited ):
            return False

        return True;

    def _get_my_position(self):
        for i, x in enumerate(grid):
            if 'm' in x:
                return (i, x.index('m'))

    def _got_queen(self):
        if self.grid[self.current_track[-1][X]][self.current_track[-1][Y]] == 'p':
            return True
        return False

    def _parse_steps(self, steps):
        for i, items in enumerate(steps[:-1]):
            if steps[i][X]-steps[i+1][X] == 1 and steps[i][Y]-steps[i+1][Y] == 0:
                print "UP"
            elif steps[i][X]-steps[i+1][X] == -1 and steps[i][Y]-steps[i+1][Y] == 0:
                print "DOWN"
            elif steps[i][X]-steps[i+1][X] == 0 and steps[i][Y]-steps[i+1][Y] == -1:
                print "RIGHT"
            elif steps[i][X]-steps[i+1][X] == 0 and steps[i][Y]-steps[i+1][Y] == 1:
                print "LEFT"


def displayPathtoPrincess(n,grid):
    bot = mybot(n, grid)
    bot.find_move()
#print all the moves here
# Tail starts here

m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
