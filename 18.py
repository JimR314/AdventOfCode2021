import math
import os
import time
from collections import *

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '18.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

def explode(num):
    stack = 0
    do = False
    start = 0
    end = 0
    comma = 0
    for i, char in enumerate(num):
        if char == '[':
            stack += 1
        elif char == ']':
            stack -= 1
        if stack >= 5 and char == '[':
            do = True
            start = i
        if do and char == ']':
            end = i
            do = False
            break
    if start == 0 or end == 0:
        return num
    for i in range(start, end):
        if num[i] == ',':
            comma = i
    for i in range(start, -1, -1):
        done = False
        td = False
        dd = False
        if i >= 1:
            if num[i] != '[' and num[i] != ']' and num[i] != ',':
                index = i
                if num[i-1] != '[' and num[i-1] != ']' and num[i-1] != ',':
                    number = int(num[i-1]+num[i]) + int(num[start+1:comma])
                    done = True
                    td = True
                    break
                else:
                    number = int(num[i]) + int(num[start+1:comma])
                    done = True
                    break
        elif i < 1 and not done:
            break
    if done:
        if number >= 10 and not td:
            dd = True
        if td:
            num = num[:index-1] + str(number) + num[index+1:]
        else:
            num = num[:index] + str(number) + num[index+1:]
    if dd:
        start += 1
        end += 1
        comma += 1
    for i in range(end, len(num)):
        done = False
        td = False
        if i <= len(num):
            if num[i] != '[' and num[i] != ']' and num[i] != ',':
                index = i
                if num[i+1] != '[' and num[i+1] != ']' and num[i+1] != ',':
                    number = int(num[i]+num[i+1]) + int(num[comma+1:end])
                    done = True
                    td = True
                    break
                else:
                    number = int(num[i]) + int(num[comma+1:end])
                    done = True
                    break
        elif i > len(num) and not done:
            break
    if done:
        if td:
            num = num[:index] + str(number) + num[index+2:]
        else:
            num = num[:index] + str(number) + num[index+1:]
    
    num = num[:start] + '0' + num[end+1:]
    return num

def split(num):
    chars = ['[', ']', ',']
    for i, char in enumerate(num):
        if i != len(num)-1:
            if num[i] not in chars and num[i+1] not in chars:
                number = int(num[i]+num[i+1])
                if number % 2 == 0:
                    num = num[:i] + '[' + str(number//2) + ',' + str(number//2) + ']' + num[i+2:]
                    break
                else:
                    num = num[:i] + '[' + str(number//2) + ',' + str(number//2 + 1) + ']' + num[i+2:]
                    break
    return num

def adder(num):
    while True:
        if num == explode(num) and num == split(num):
            break
        elif num == explode(num):
            num = split(num)
        else:
            num = explode(num)
    return num

def magnitude(num):
    start = 0
    end = 0
    comma = 0
    for i, char in enumerate(num):
        if char == '[':
            start = i
        if char == ']':
            end = i
            break
    for i in range(start, end):
        if num[i] == ',':
            comma = i
    if not (start == 0 and end == 0 and comma == 0):
        num = num[:start] + str(3*int(num[start+1:comma]) + 2*int(num[comma+1:end])) + num[end+1:]
    return num

'''
run = lines[0]
for i, line in enumerate(lines):
    if i != 0:
        string = '[' + run + ',' + line + ']'
        #print(string)
        run = adder(string)

while True:
    if magnitude(run)[0] != '[':
        print(magnitude(run))
        break
    else:
        run = magnitude(run)'''

li = []
for i in range(100):
    print(i)
    for j in range(100):
        if i != j:
            string = '[' + lines[i] + ',' + lines[j] + ']'
            run = adder(string)
            while True:
                if magnitude(run)[0] != '[':
                    num = (magnitude(run))
                    break
                else:
                    run = magnitude(run)
            li.append(int(num))
print(max(li))

print(f'The program took {time.perf_counter()} seconds')