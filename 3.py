import os
import time
import math

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '3.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

'''
g = ''
tots = [0 for i in range(12)]
for i,line in enumerate(lines):
    for x,char in enumerate(line):
        tots[x] += int(char)
for count in tots:
    if count > 500:
        g  = g + '1'
    else:
        g = g + '0'

print(tots, g)

inverse_s = ''
  
for i in g:
    
    if i == '0':
        inverse_s += '1'
          
    else:
        inverse_s += '0'


print(g, inverse_s)
print(int(g), inverse_s)
#print(int(g, 2))

'''

remaining = [line for line in lines]
copy = [line for line in remaining]
for i in range(12):
    remaining = [line for line in copy]
    count = 0
    for line in remaining:
        count += int(line[i])
    length = math.ceil(len(remaining)/2)
    for line in remaining:
        if count < (length) and line[i] == '1':
            copy.remove(line)
        elif count >= length and line[i] == '0':
            copy.remove(line)
    if len(copy) == 1:
        print(copy)
        break

remaining = [line for line in lines]
copy = [line for line in remaining]
for i in range(12):
    remaining = [line for line in copy]
    count = 0
    for line in remaining:
        count += int(line[i])
    length = math.ceil(len(remaining)/2)
    for line in remaining:
        if count < (length) and line[i] == '0':
            copy.remove(line)
        elif count >= length and line[i] == '1':
            copy.remove(line)
    if len(copy) == 1:
        print(copy)
        break   

print(f'The program took {time.perf_counter() - start:0.4f} seconds')