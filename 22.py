import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '22.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

def intersect(cuboid, x1, x2, y1, y2, z1, z2):
    if x2 < cuboid[0] or x1 > cuboid[1] or y2 < cuboid[2] or y1 > cuboid[3] or z2 < cuboid[4] or z1 > cuboid[5]:
        return False
    else:
        startx = cuboid[0] if x1 <= cuboid[0] else x1
        endx = cuboid[1] if x2 >= cuboid[1] else x2
        starty = cuboid[2] if y1 <= cuboid[2] else y1
        endy = cuboid[3] if y2 >= cuboid[3] else y2
        startz = cuboid[4] if z1 <= cuboid[4] else z1
        endz = cuboid[5] if z2 >= cuboid[5] else z2
        return startx, endx, starty, endy, startz, endz

def volume(a, b, c, d, e, f):
    return (abs(b-a)+1)*(abs(d-c)+1)*(abs(f-e)+1)

#Part 2
'''
order = []
for k, line in enumerate(lines):
    p1, p2 = line.split(' ')
    x, y, z = p2.split(',')
    x1, x2 = x[2:].split('..')
    y1, y2 = y[2:].split('..')
    z1, z2 = z[2:].split('..')
    x1,x2,y1,y2,z1,z2 = [int(j) for j in [x1,x2,y1,y2,z1,z2]]

    if p1 == 'on':
        order.append((1, (x1, x2, y1, y2, z1, z2)))

    for i, box in enumerate(order[:-1]):
        if intersect(box[1], x1, x2, y1, y2, z1, z2) != False:
            if box[0] == 0 and p1 == 'on':
                order.append((1, intersect(box[1], x1, x2, y1, y2, z1, z2)))
            elif box[0] == 1 and p1 == 'off':
                order.append((0, intersect(box[1], x1, x2, y1, y2, z1, z2)))
            elif box[0] == 0 and p1 == 'off':
                order.append((1, intersect(box[1], x1, x2, y1, y2, z1, z2)))
            elif box[0] == 1 and p1 == 'on':
                order.append((0, intersect(box[1], x1, x2, y1, y2, z1, z2)))

print(len(order))
for box in order:
    a, b, c, d, e, f = box[1]
    if box[0] == 0:
        total -= volume(a, b, c, d, e, f)
    elif box[0] == 1:
        total += volume(a, b, c, d, e, f)
    else:
        print('uh oh')
print(total)'''


#Part 1
'''
points = set()
for line in lines:
    p1, p2 = line.split(' ')
    x, y, z = p2.split(',')
    x1, x2 = x[2:].split('..')
    y1, y2 = y[2:].split('..')
    z1, z2 = z[2:].split('..')
    x1,x2,y1,y2,z1,z2 = [int(j) for j in [x1,x2,y1,y2,z1,z2]]
    if x1 >= -50 and x2 <= 50 and y1 >= -50 and y2 <= 50 and z1 >= -50 and z2 <= 50:
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                for c in range(z1, z2+1):
                    if p1 == 'on':
                        points.add((a, b, c))
                    elif (a, b, c) in points:
                        points.remove((a, b, c))
    print(len(points))'''

print(f'The program took {time.perf_counter()} seconds')