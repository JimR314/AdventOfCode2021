import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '20.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

grid = []
points = set()

for y, line in enumerate(lines):
    if y == 0:
        data = line
    elif line != '':
        grid.append(line)

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '#':
            points.add((x, y))

def findBounds(points): #This is absolutely a terrible waste of time, but idk how to code it faster. Maybe a lambda or something fancy?
    for i, (x, y) in enumerate(points):
        if i == 0:
            minx = x
            maxx = x
            miny = y
            maxy = y
        else:
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
    return minx, maxx, miny, maxy

def returnScore(x, y, points):
    s = ''
    for m in range(-1, 2): #Iterate from -1 to 1 for x coords
        for n in range(-1, 2): #Iterate from -1 to 1 for y coords
            if (x+n, y+m) in points:
                s += '1'
            else:
                s += '0'
    return s #Return string formed

#Part 1
'''
for n in range(2):
    minx, maxx, miny, maxy = findBounds(points)
    newpoints = copy.deepcopy(points)
    for y in range(miny - 10, maxy + 10):
        for x in range(minx - 10, maxx + 10):
            value = int(returnScore(x, y, points), 2)
            lit = data[value]
            if lit == '#' and (x, y) not in points:
                newpoints.add((x, y))
            elif lit == '.' and (x, y) in points:
                newpoints.remove((x, y))
    points = copy.deepcopy(newpoints)
    print(len(points))

for (x, y) in points:
    if x >= -2 and x <= 101:
        if y >= -2 and y <= 101:
            total += 1
print(total)'''

#Part 2
for m in range(1, 26): #I'm doing the steps in pairs so the infinite region is always off after every pair
    for n in range(2):
        minx, maxx, miny, maxy = findBounds(points) #Find the bounds of the region
        newpoints = copy.deepcopy(points)
        for y in range(miny - 50, maxy + 52): #Not taking any chances
            for x in range(minx - 50, maxx + 52):
                value = int(returnScore(x, y, points), 2) #Get the binary string to an int
                lit = data[value] #Find the corresponding value of that in the data
                if lit == '#' and (x, y) not in points: #Change it if it needs to be changed
                    newpoints.add((x, y))
                elif lit == '.' and (x, y) in points: #Change it if it needs to be changed
                    newpoints.remove((x, y))
        points = newpoints
    newpoints = copy.deepcopy(points)
    for (x, y) in points: #Remove all points that aren't in the 'box' created every other step (when the infinite expanse is all off)
        if x >= -2*m and x <= 99+2*m:
            if not (y >= -2*m and y <= 99+2*m):
                newpoints.remove((x, y))
        else:
            newpoints.remove((x, y))
    points = newpoints    
print(len(points))

print(f'The program took {time.perf_counter()} seconds')