import os
import time
import math
from collections import *

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '6.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

'''
nums = lines[0].split(',')
for i in range(256):
    #print(i)
    copy =[i for i in nums]
    for i, num in enumerate(nums):
        #print(num)
        if int(num) > 0:
            copy[i] = str(int(num)-1)
        else:
            copy[i] = '6'
            copy.append('8')
    nums = copy
print(len(nums))
'''
nums = [int(i) for i in lines[0].split(',')]
cnt = Counter(nums)
li = [[i, cnt[i]] for i in range(9)]

for i in range(256):
    copy = [x for x in li]
    clone = li[0][1]
    for x in range(8):
        copy[x][1] = li[x+1][1]
    copy[8][1] = clone
    copy[6][1] += clone
    li = copy
for i in range(9):
    total += li[i][1]
print(total)
'''
def Calc(li, days):
    if days == 1:
        return (2, li) if li[0]=='0' else (1, li)
    elif days > 1:
        if li[0] != '0':
            if days > 8:
                num = int(li[0])
                li[0] = '0'
                num, going1 = Calc(li, days-num)
                return(num, going1)
            else:
                li[0] = str(int(li[0])-1)
                num, going1 = Calc(li, days-1)
                return(num, going1)
        else:
            if days > 8:
                li[0] = '1'
                num1, going1 = Calc(li, days-6)
                li1 = ['1']
                num2, going2 = Calc(li1, days-8)
            else:
                li[0] = '6'
                num1, going1 = Calc(li, days-1)
                li1 = ['8']
                num2, going2 = Calc(li1, days-1)
            #print('hi', li + li1)
            return(num1+num2, going1+going2)
        
        copy =[i for i in li]
        for i, num in enumerate(li):
            if int(num) > 0:
                copy[i] = str(int(num)-1)
            else:
                copy[i] = '6'
                copy.append('8')
        li = copy
        li.sort()
        return(len(li))
        
copy = ['1']
def Calc1(num, days):
    day50, li50 = Calc([num], days+1)
    day49, li49 = Calc([num], days)
    li51 = [int(x) for x in li50]
    li51.sort()
    return (day49, li51)

print(Calc1('5', 51))

day50, li50 = Calc([1], 10)
day49, li49 = Calc([1], 9)
print(day49, li50) #After 9 days
#print(Calc(newLi, 256) * cnt[1])
#print(len(nums))
'''

print(f'The program took {time.perf_counter() - start:0.4f} seconds')