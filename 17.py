import math
import os
import time
from collections import *

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '17.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')
total = 0

for line in lines:
    p2 = line.split('a: ')[1]
    x, y = p2.split(', ')
    x1, x2 = x[2:].split('..')
    y1, y2 = y[2:].split('..')
print(x1, x2, y1, y2)
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
count = 0
while True:
    count += 1
    total += count
    if (total) <= max(x1, x2) and total >= min(x1, x2):
        print(total, count)
    if (total+count+1) > max(x1, x2):
        break
print(total, count)
yI = 67
xI = count
x = 0
y = 0
bigLi = 0
for j in range(300):
    yValues = []
    for i in range(-100, 200):
        yI = i
        xI = count+j
        c = 0
        x = 0
        y = 0
        while True:
            if xI-c >= 0:
                x += xI-c
            y += yI-c
            c += 1
            if y <= -44 and y >= -68 and x >= 269 and x <= 292:
                #print(x, y)
                yValues.append(yI)
                break
            elif y < -68:
                break
    bigLi += len(yValues)
    print(bigLi, j+count)
print(bigLi)
#8-67
'''
c = 0
yMax = 0
while True:
    if xI-c >= 0:
        x += xI-c
    y += yI-c
    if y > yMax:
        yMax = y
    c += 1
    if y <= -44 and y >= -98:
        print(x, y, yMax)
        break'''




print(f'The program took {time.perf_counter()} seconds')