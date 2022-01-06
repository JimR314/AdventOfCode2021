import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '9.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

newli = []
for line in lines:
    line = '9' + line
    line += '9'
    newli.append(line)
newli.insert(0, ('9'*102))
newli.append(('9'*102))
lines = newli
'''
for y, line in enumerate(lines):
    for i, char in enumerate(line):
        if y == 1 and i == 9: print(int(char))
        if i != 0 and i != (len(line)-1)  and y > 0 and y < len(lines)-1:
            if int(char) < int(line[i-1]) and int(char) < int(line[i+1]):
                if int(char) < int(lines[y-1][i]):
                    if int(char) < int(lines[y+1][i]):
                        #print(int(char), i, y)
                        total += int(char) + 1

print(total)
'''
def isNextTo(a, b, x, y):
    if a == x and abs(y-b) == 1 or b == y and abs(x-a) == 1:
        return True
    return False

basins = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != '9':
            basins.append([(x, y)])
length = len(basins)
while True:
    print(length)
    print(basins)
    for i, basin in enumerate(basins):
        if [(5, 4)] in basins: print('ye', basin)
        else: print('nah', basin)
        copy = [j for j in basin]
        for x, y in basin:
            conc = False
            for j, oBasin in enumerate(basins):
                if i != j:
                    for a, b in oBasin:
                        if isNextTo(a, b, x, y):
                            conc = True
                            adj = oBasin
                            place = j
                            break
                    if conc:
                        break
            if conc:
                copy = copy + adj
                del basins[place]
        if not conc or (conc and i < place):
            basins[i] = copy
        else:
            basins[i-1] = copy
    if len(basins) == length:
        break
    length = len(basins)
for line in lines:
    print(line)
for i, basin in enumerate(basins):
    basins[i] = list(dict.fromkeys(basin))
lens = [len(li) for li in basins]
print(basins)
a = max(lens)
lens.remove(a)
b = max(lens)
lens.remove(b)
c = max(lens)
lens.remove(c)
print(a, b, c, a*b*c)
'''
for i, start in enumerate(basins):
    for j, comp in enumerate(basins):
        if i != j:
            for a, b in comp:
                for x, y in start:
                    if isNextTo(a, b, x, y):
                        conc = True'''
'''
for y, line in enumerate(lines):
    start = False
    for x, char in enumerate(line):
        num = int(char)
        if num != 9:
            adj = False
            for c, basin in enumerate(basins):
                if (x, y) not in basin:
                    bCopy = [i for i in basin]
                    for a, b in basin:
                        if isNextTo(a, b, x, y):
                            adj = True
                            change = c
                            bCopy.append((x, y))
                            break
                    if adj:
                        basins[change] = bCopy
                        break
            if not adj:
                basins.append([(x, y)])
print(f'The program took {time.perf_counter() - start:0.4f} seconds')
length = len(basins)
print(length)
while True:
    print(length)
    for i, basin in enumerate(basins):
        copy = [j for j in basin]
        for x, y in basin:
            conc = False
            for j, oBasin in enumerate(basins):
                if i != j:
                    for a, b in oBasin:
                        if isNextTo(a, b, x, y):
                            conc = True
                            adj = oBasin
                            place = j
                            break
                    if conc:
                        break
            if conc:
                copy = copy + adj
                del basins[place]
        if not conc or (conc and i < place):
            basins[i] = copy
        else:
            basins[i-1] = copy
    if len(basins) == length:
        break
    length = len(basins)

lens = [len(li) for li in basins]
a = max(lens)
lens.remove(a)
b = max(lens)
lens.remove(b)
c = max(lens)
lens.remove(c)
print(a, b, c, a*b*c)'''

print(f'The program took {time.perf_counter() - start:0.4f} seconds')