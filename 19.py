import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '19.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0
counter = 0

length = 100
scanners = [[] for i in range(length)]
sr = [[] for i in range(length)] #direction vectors for every scanner
sr[0] = [0, 1, 2]
sl = [[] for i in range(length)]
sl[0] = (0, 0, 0)
so = [[] for i in range(length)]
so[0] = (1, 1, 1)
s = False
for i, line in enumerate(lines):
    if line[:3] == '---':
        s = True
    elif line == '':
        s = False
        counter += 1
    elif s == True:
        nums = list(map(int, line.split(',')))
        scanners[counter].append([nums[0], nums[1], nums[2]])

scannersCopy = copy.deepcopy(scanners)

rotations = list(itertools.permutations([0, 1, 2], 3))
li = []
for x in range(-1, 3, 2):
    for y in range(-1, 3, 2):
        for z in range(-1, 3, 2):
            li.append([x,y,z])

stack = [0]
dealt = [0]
order = []
while len(stack) > 0:
    h = stack.pop()
    dealt.append(h)
    for j in range(length):
        if j != h and j not in dealt:
            for ord in li:
                for rotation in rotations:
                    places = defaultdict(int)
                    for nums1 in scanners[h]:
                        for nums2 in scanners[j]:
                            coords = [nums2[i] for i in rotation]
                            coords = [c*ord[x] for x, c in enumerate(coords)]
                            location = (nums1[0]-coords[0], nums1[1]-coords[1], nums1[2]-coords[2])
                            places[location] += 1
                    for key in places:
                        if places[key] >= 12:
                            if sl[j] == []:
                                sl[j] = key
                            if sr[j] == []:
                                sr[j] = rotation
                            if so[j] == []:
                                so[j] = ord
                            if j not in stack:
                                stack.append(j)
                            if ([j, h]) not in order:
                                order.append([h, j])
                            for y, nums1 in enumerate(scanners[j]):
                                v = [nums1[i] for i in rotation]
                                v = [c*ord[x] for x, c in enumerate(v)]
                                scanners[j][y] = v

relative = [[] for i in range(len(scanners))]
relative[0] = scanners[0]

order2 = []
for ord in order:
    if ord not in order2:
        order2.append(ord)
order = order2

done = [0]
for pair in order:
    if pair[1] not in done:
        sl[pair[1]] = [sl[pair[0]][i]+sl[pair[1]][i] for i in range(3)]
        done.append(pair[1])

for i in range(len(so)):
    so[i] = list(so[i])
    sr[i] = list(sr[i])

beacons = []
bSet = set()
for i, scanner in enumerate(scannersCopy):
    for beacon in scanner:
        v = [beacon[x] for x in sr[i]]
        v = [c*so[i][x] for x, c in enumerate(v)]
        location = [(v[x] + sl[i][x]) for x in range(3)]
        if location not in beacons:
            total += 1
            beacons.append(location)
        bSet.add(tuple(location))

#Part 1
print(total)

#Part 2
total = 0
for y, i in enumerate(sl):
    if i != []:
        for x, j in enumerate(sl):
            if x != y and j != []:
                value = sum([abs(j[a]-i[a]) for a in range(3)])
                if value > total:
                    total = value
print(total)

print(f'The program took {time.perf_counter()} seconds')