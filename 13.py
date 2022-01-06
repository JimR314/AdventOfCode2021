import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '13.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')
total = 0

coords = []
folds = []
cont = True
for line in lines:
    if line == '':
        cont = False
    elif cont:
        x, y = line.split(',')
        coords.append((x, y))
    else:
        axis, num = (line.split())[2].split('=')
        folds.append((axis, num))

def fold(coords, axis, num, w, h):
    new = [i for i in coords]
    newer = []
    for i, (x, y) in enumerate(coords):
        if axis == 'y':
            if int(y) > int(num):
                new[i] = (x, str(2*int(num) - int(y)))
        if axis == 'x':
            if int(x) > int(num):
                new[i] = (str(2*int(num) - int(x)), y)
    for i, (x, y) in enumerate(new):
        if axis == 'y':
            if int(y) < int(num):
                if (x, y) not in newer:
                    newer.append((x, y))
        if axis == 'x':
            if int(x) < int(num):
                if (x, y) not in newer:
                    newer.append((x, y))
    if axis == 'y' and int(y) > 100:
        h = (h-1)//2
    if axis == 'x':
        w = (w-1)//2
    return newer, h, w

def findSize(coords):
    h = 0
    w = 0
    for (x, y) in coords:
        if int(x) > w:
            w = int(x)
        if int(y) > h:
            h = int(y)
    return h, w

grid = [i for i in coords]
for i, f in enumerate(folds):
    hei, wid = (findSize(grid))
    grid, h, w = fold(grid, f[0], f[1], wid, hei)
    tot = len(grid)
    print(tot)
for i in range(h):
    s = ''
    for j in range(w):
        if (str(j), str(i)) not in grid:
            s += '.'
        else:
            s += '#'
    print(s)


print(f'The program took {time.perf_counter() - start:0.4f} seconds\n')