from math import sqrt
import math

class agent(object):

    def __init__(self, hall, notation='X', mirror_notation='#'):
        self.hall = hall
        self.notation = notation
        self.mirror_notation = mirror_notation
        self.position = self.__get_position()
    
    def __get_position(self):
        for row_count, row in enumerate(self.hall):
            for column_count, column in enumerate(row):
                if self.hall[row_count][column_count] == self.notation:
                    return { 'r': row_count, 'c': column_count }
        raise Exception("Agent position not found")

    def look_up(self):
        reflection = 0.5
        for up_range in reversed(range(0, self.position['r'])):
            if self.hall[up_range][self.position['c']] == self.mirror_notation:
                    print "There is a mirror at : %d %d" % (up_range, self.position['c'])
                    return reflection*2
                    break
            reflection += 1

def reflect_mirror_hall(mirror_hall):
    for row_count, row in enumerate(mirror_hall):
        mirror_hall[row_count].append('#')
        mirror_hall[row_count].insert(0,'#')

  
    mirror_hall.insert(0, [item for item in mirror_hall[0]])
    mirror_hall.append([item for item in mirror_hall[0]])
    

def dist(x1,y1,x2,y2):
    return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def angle(x1,y1,x2,y2):
    angleR = math.atan2(x2-x1, y2-y1)
    return math.degrees(angleR)

done_angle = []
answer = 0
D = 2

def do_calculation(mirror_hall):
    global answer
    global D
    global done_angle

    me = agent(mirror_hall)
    print me.position

    column_boundary = len(mirror_hall[0]) 
    row_boundary = len(mirror_hall)

    boundary_index = [(r,c) for r in range(0, row_boundary) for c in range(0, column_boundary) if r==0 or c==0 or r== (row_boundary-1) or c== (column_boundary-1)]

    print boundary_index
    for index in boundary_index:
        r = list(index)[0]
        c = list(index)[1]
        distance = dist(r, c, me.position['r'], me.position['c'])
        ang = angle(r, c, me.position['r'], me.position['c'])
        if distance <= D and ang not in done_angle:
            print (distance, ang)
            done_angle.append(ang)
            answer += 1
    '''
    for row_count, row in enumerate(mirror_hall):
        for column_count, column in enumerate(row):
            if mirror_hall[row_count][column_count] == '#':
                print (row_count, column_count)
                print dist(row_count, column_count, me.position['r'], me.position['c'])
                print angle(row_count, column_count, me.position['r'], me.position['c'])
    '''

def main():
    import pprint

    mirror_hall = [
                ['#','#','#'],
                ['#','X','#'],
                ['#','.','#'],
                ['#','#','#']
              ]

    do_calculation(mirror_hall)
    #2
    #reflect_mirror_hall(mirror_hall)
    #do_calculation(mirror_hall)
    
    
    
    
    
    

    print answer
    #print done_angle
    

if __name__ == "__main__":
    main()
