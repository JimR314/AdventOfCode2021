import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '21.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

p1 = 8
p2 = 1
p1t = 0
p2t = 0

turn = 1
count = 1

#1 2 3
#2 3 4  3 4 5  4 5 6
#3 4 5  4 5 6  5 6 7   4 5 6  5 6 7  6 7 8    5 6 7  6 7 8  7 8 9
#1 3, 3 4, 6 5, 7 6, 6 7, 3 8, 1 9

cases = defaultdict(int)
cases[(p1, p2, 0, 0)] = 1
while True:
    t1 = p1t
    t2 = p2t
    clone = copy.deepcopy(cases)
    if turn == 1:
        for (x, y, a, b) in cases:
            num = cases[(x, y, a, b)]
            if num != 0:
                clone[((x+3-1)%10+1, y, a+(x+3-1)%10+1, b)] += 1*num
                clone[((x+4-1)%10+1, y, a+(x+4-1)%10+1, b)] += 3*num
                clone[((x+5-1)%10+1, y, a+(x+5-1)%10+1, b)] += 6*num
                clone[((x+6-1)%10+1, y, a+(x+6-1)%10+1, b)] += 7*num
                clone[((x+7-1)%10+1, y, a+(x+7-1)%10+1, b)] += 6*num
                clone[((x+8-1)%10+1, y, a+(x+8-1)%10+1, b)] += 3*num
                clone[((x+9-1)%10+1, y, a+(x+9-1)%10+1, b)] += 1*num
                clone[(x, y, a, b)] -= num
    else:
        for (x, y, a, b) in cases:
            num = cases[(x, y, a, b)]
            if num != 0:
                clone[(x, (y+3-1)%10+1, a, b+(y+3-1)%10+1)] += 1*num
                clone[(x, (y+4-1)%10+1, a, b+(y+4-1)%10+1)] += 3*num
                clone[(x, (y+5-1)%10+1, a, b+(y+5-1)%10+1)] += 6*num
                clone[(x, (y+6-1)%10+1, a, b+(y+6-1)%10+1)] += 7*num
                clone[(x, (y+7-1)%10+1, a, b+(y+7-1)%10+1)] += 6*num
                clone[(x, (y+8-1)%10+1, a, b+(y+8-1)%10+1)] += 3*num
                clone[(x, (y+9-1)%10+1, a, b+(y+9-1)%10+1)] += 1*num
                clone[(x, y, a, b)] -= num
    for (x, y, a, b) in clone:
        if a >= 21:
            p1t += clone[(x, y, a, b)]
            clone[(x, y, a, b)] = 0
        elif b >= 21:
            p2t += clone[(x, y, a, b)]
            clone[(x, y, a, b)] = 0
    if t1 == p1t and t2 == p2t and t1 != 0 and t2 != 0:
        print(max(p1t, p2t))
        break        
    cases = clone
    if turn == 1:
        turn = 2
    else:
        turn = 1

'''
while True:
    print(p1t, p2t)
    if p1t >= 1000:
        print(p2t*(count-1), p2t, count)
        break
    elif p2t >= 1000:
        print(p1t*(count-1), p1t, count)
        break
    else:
        if turn == 1:
            for i in range(3):
                p1 = (p1+count-1)%10+1
                count += 1
            p1t += p1
        else:
            for i in range(3):
                p2 = (p2+count-1)%10+1
                count += 1
            p2t += p2
    if turn == 1:
        turn = 2
    else:
        turn = 1'''

print(f'The program took {time.perf_counter()} seconds')