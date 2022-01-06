import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '25.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

grid = []
for line in lines:
    grid.append([i for i in line])

#137, 139
moves = 0
while True:
    c = moves
    for y, line in enumerate(grid):
        lineC = copy.deepcopy(line)
        for x, char in enumerate(line):
            if x < len(line)-1:
                if char == '>' and line[x+1] == '.':
                    moves += 1
                    lineC[x] = '.'
                    lineC[x+1] = '>'
            elif x == len(line)-1:
                if char == '>' and line[0] == '.':
                    moves += 1
                    lineC[x] = '.'
                    lineC[0] = '>'
        grid[y] = lineC
    gridC = copy.deepcopy(grid)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == 'v' and y < len(grid)-1:
                if grid[y+1][x] == '.':
                    moves += 1
                    gridC[y+1][x] = 'v'
                    gridC[y][x] = '.'
            elif char == 'v' and y == len(grid)-1:
                if grid[0][x] == '.':
                    moves += 1
                    gridC[0][x] = 'v'
                    gridC[y][x] = '.'
    grid = gridC
    total += 1
    if total%100==0:print(total)
    if c == moves:
        break
    c = moves
print(total)

                    
print(f'The program took {time.perf_counter()} seconds')