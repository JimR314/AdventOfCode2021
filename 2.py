import os
import time

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '2.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

totalx = 0
totaly = 0
aim = 0
for i, line in enumerate(lines):
    #print(totalx, totaly, aim)
    chars = line.split(' ')
    if chars[0] == 'forward':
        #print(chars)
        totalx += int(chars[1])
        totaly += aim*int(chars[1])
    elif chars[0] == 'down':
        #totaly += int(chars[1])
        aim += int(chars[1])
    elif chars[0] == 'up':
        #totaly -= int(chars[1])
        aim -= int(chars[1])

print(totaly, totalx, totalx*totaly,aim)
print(f'The program took {time.perf_counter() - start:0.4f} seconds')