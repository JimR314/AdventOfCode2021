import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '8.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

'''
for line in lines:
    chars = line.split(' | ')
    output = chars[1]
    outputs = output.split()
    lens = [2, 3, 4, 7]
    for num in outputs:
        if len(num) in lens:
            total += 1
print(total)
'''

for line in lines:
    inp, out = line.split(' | ')
    inps = inp.split()
    #p{Num} represents which string is which number
    for num in inps:
        if len(num) == 3:
            p7 = num
        if len(num) == 2:
            p1 = num
    a = list(set(p7)-set(p1))[0] #Intersection of 7 and 1 gives a
    for num in inps:
        if len(num) == 4:
            p4 = num
        if len(num) == 7:
            p8 = num
        if len(num) == 6:
            p6 = num
            ls = [i for i in p6 if i in p1]
            if len(ls) == 1:
                f = ls[0]
                c = [i for i in p1 if i != f][0]
                p6done = p6
    fives = []
    for num in inps:
        if len(num) == 6:
            notIn = [i for i in p8 if i not in num][0]
            if notIn != c and notIn in p4:
                d = notIn
    for num in inps:
        if len(num) == 6 and num != p6done and d not in num:
            p0 = num
        elif len(num) == 6 and num != p6done and d in num:
            p9 = num
        if len(num) == 5:
            fives.append(num)
    for char in p4:
        if char != c and char != d and char != f:
            b = char
    for char in p9:
        if char != c and char != d and char != f and char != a and char != b:
            g = char
    for char in p0:
        if char != c and char != f and char != a and char != b and char != g:
            e = char
    number = ''
    for num in out.split():
        if len(num) == 2:
            number += '1'
        if len(num) == 3:
            number += '7'
        if len(num) == 4:
            number += '4'
        if len(num) == 7:
            number += '8'
        if len(num) == 5:
            if b in num:
                number += '5'
            elif e in num:
                number += '2'
            else:
                number += '3'
        if len(num) == 6:
            if c not in num:
                number += '6'
            if e not in num:
                number += '9'
            if d not in num:
                number += '0'
    total += int(number)
    #print(number, a, b, c, d, e, f, g)
print(total)

print(f'The program took {time.perf_counter() - start:0.4f} seconds')
