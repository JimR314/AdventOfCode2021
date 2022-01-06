import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '24.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')


total = 0

w, x, y, z = ['' for i in range(4)]


instructions = []
for i, line in enumerate(lines):
    if line[:3] == 'inp':
        li = [line]
    else:
        li.append(line)
        if i == len(lines)-1 or lines[i+1][:3] == 'inp':
            instructions.append(li)


digits = ''
dict = defaultdict(int)

def maximum(instruction, j, di, digits):
    #print(j, di)
    #print(instruction)
    if j == 13:
        i = digits[0] - 6
        dict = copy.deepcopy(di)
        valid = True
        dict['w'] = i
        dict['x'] = int((dict['z']%26)+int(instruction[5].split(' ')[2]) != dict['w'])
        dict['z'] //= int(instruction[4].split(' ')[2])
        dict['z'] *= 25*dict['x'] + 1
        dict['z'] += (dict['w'] + int(instruction[15].split(' ')[2]))*dict['x']
        if valid and dict['z'] == 0:
            print(str(i))
            return str(i)
        return False
    else:
        for i in range(9, 0, -1):
            #print(digits)
            digits.append(i)
            if (j == 3 and digits[2] + 7 == i) or (j == 5 and digits[4] + 1 == i) or (j == 9 and digits[8] + 8 == i) or (j == 10 and digits[7] + 6 == i) or (j == 11 and digits[6] - 1 == i) or (j == 12 and digits[1] - 2 == i) or (j == 13 and digits[0] - 6 == i) or j in [0, 1, 2, 4, 6, 7, 8]:
                #if j <= 8 :print(j, i)
                dict = copy.deepcopy(di)
                valid = True
                dict['w'] = i
                dict['x'] = int((dict['z']%26)+int(instruction[5].split(' ')[2]) != dict['w'])
                dict['z'] //= int(instruction[4].split(' ')[2])
                dict['z'] *= 25*dict['x'] + 1
                dict['z'] += (dict['w'] + int(instruction[15].split(' ')[2]))*dict['x']
                if valid:
                    #b = copy.deepcopy(dict)
                    #b['z'] = 0
                    digits.append(i)
                    v = maximum(instructions[j+1], j+1, dict, copy.deepcopy(digits))
                    if v != False:
                        print(str(i)+v)
                        return str(i)+v
            '''
            for line in instruction:
                if line[:3] == 'inp':
                    op, a = line.split(' ')
                    dict[a] = i
                else:
                    op, a, b = line.split(' ')
                    if b.isnumeric() or b[0] == '-':
                        b = int(b)
                        if op == 'add':
                            dict[a] = dict[a] + b
                        elif op == 'mul':
                            dict[a] = dict[a] * b
                        elif op == 'eql':
                            dict[a] = 1 if dict[a]==b else 0
                        elif op == 'div' and b != 0:
                            dict[a] = dict[a] // b
                        elif op == 'mod' and dict[a] >= 0 and b > 0:
                            dict[a] = dict[a] % b
                        else:
                            valid = False
                            break
                    else:
                        if op == 'add':
                            dict[a] = dict[a] + dict[b]
                        elif op == 'mul':
                            dict[a] = dict[a] * dict[b]
                        elif op == 'eql':
                            dict[a] = 1 if dict[a]==dict[b] else 0
                        elif op == 'div' and dict[b] != 0:
                            dict[a] = dict[a] // dict[b]
                        elif op == 'mod' and dict[a] >= 0 and dict[b] > 0:
                            dict[a] = dict[a] % dict[b]
                        else:
                            valid = False
                            break'''
        return False

print(maximum(instructions[0], 0, dict, []))
                    
print(f'The program took {time.perf_counter()} seconds')