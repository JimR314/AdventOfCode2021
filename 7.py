import math
import os
import time
from collections import *

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '7.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0
totals = []
best = 1000000000

numbers = [int(i) for i in lines[0].split(',')]
numbers.sort()

print(sum(numbers)/len(numbers))
'''
squares = [i*(i+1)//2 for i in numbers]
sumN = sum(numbers)
sumS = sum(squares)
length = len(squares)
print(numbers[695:706])
print((sumS / length)**0.5)
'''
print(len(numbers))
for j in range(1, 1000):
    total = 0
    for i, num in enumerate(numbers):
        x = abs(numbers[j] - num)
        total += (x**2 + x)//2
    totals.append(total)
    if total < best:
        best = total
        print(best, 'HERE', j)

print(f'The program took {time.perf_counter() - start:0.4f} seconds')