import numpy as np
import math

#arr = np.arange(0,15).reshape([3,5])

arr = np.array([
                ['#','#','#'],
                ['#','X','#'],
                ['#','.','#'],
                ['#','#','#']
              ])

def reflect_axis_y(arr):
    a = np.copy(arr)
    i = 0
    j = a.shape[1]-1

    while i<=j:
        temp = np.copy(a[:,i])
        a[:,i] = a[:,j]
        a[:,j] = temp
        i+=1
        j-=1
    
    return np.append(arr,a[:,1:], 1)

def reflect_axis_x(arr):
    a = np.copy(arr)
    i = 0
    j = a.shape[0]-1

    while i<=j:
        temp = np.copy(a[i,:])
        a[i,:] = a[j,:]
        a[j,:] = temp
        i+=1
        j-=1

    return np.append(arr, a[1:,:], 0)


def dist(x1,y1,x2,y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def cal_angle(x1,y1,x2,y2):
    angleR = math.atan2(x2-x1, y2-y1)
    return math.degrees(angleR)

D = 8
target = math.log(D,2)
target = int(target) if target>2 else 2

target=8
for i in range(0, target):
    arr = reflect_axis_y(arr)
    arr = reflect_axis_x(arr)




print arr

##########
search = np.where(arr=='X')
x= sorted(set(search[0]))
y= sorted(set(search[1]))
where_X = []
for count, item in enumerate(search[0]):
    where_X.append((search[0][count], search[1][count]))

my_x =  x[ len(x)//2 ]
my_y = y[ len(y)//2 ]

my_x = 7
my_x = 7

assert arr[my_x][my_y] == 'X'
##########

distance_dict = {}
for every_X in where_X:
    distance_dict[every_X] = dist(every_X[0], every_X[1], my_x, my_y)/2

#print distance_dict

import operator
sorted_dict = sorted(distance_dict.iteritems(), key=operator.itemgetter(1))

#print sorted_dict

########
done_angles = []
answer = 0
for point_X, distance in sorted_dict:
    angle = cal_angle(point_X[0], point_X[1], my_x, my_y)
    if distance != 0 and distance <= D and ( angle not in done_angles ):
        done_angles.append(angle)
        answer += 1

print answer
print done_angles


