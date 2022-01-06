import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '10.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

def addPoints(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137

tots = []
for line in lines:
    tot = 0
    n = 0
    s = 0
    c = 0
    p = 0
    stack = []
    cont = True
    for i, char in enumerate(line):
        if char == '(':
            n += 1
            stack.append(char)
        elif char == ')':
            n -= 1
            if stack[-1] != '(':
                total += 3
                cont = False
                break
            else:
                stack = stack[:-1]
        elif char == '[':
            s += 1
            stack.append(char)
        elif char == ']':
            s -= 1
            if stack[-1] != '[':
                total += 57
                cont = False
                break
            else:
                stack = stack[:-1]
        elif char == '{':
            c += 1
            stack.append(char)
        elif char == '}':
            c -= 1
            if stack[-1] != '{':
                total += 1197
                cont = False
                break
            else:
                stack = stack[:-1]
        elif char == '<':
            p += 1
            stack.append(char)
        elif char == '>':
            p -= 1
            if stack[-1] != '<':
                total += 25137
                cont = False
                break
            else:
                stack = stack[:-1]
    if len(stack) != 0 and cont:
        for char in stack[::-1]:
            tot *= 5
            if char == '(':
                tot += 1
            elif char == '[':
                tot += 2
            elif char == '{':
                tot += 3
            elif char == '<':
                tot += 4
        tots.append(tot)
tots.sort()
print(tots[(len(tots)-1)//2])
        
print(f'The program took {time.perf_counter() - start:0.4f} seconds')