import math
import os
import time
from collections import *

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '15.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')
total = 0

#Part 1
'''
lineLen = len(lines[3])+1
newli = []
for line in lines:
    newli.append(line)
newli.insert(0, (['99999']*(lineLen+1)))
newli.append((['99999']*(lineLen+1)))
lines = newli

for y, line in enumerate(lines):
    lines[y] = [i for i in line]
    if y != 0 and y != len(lines)-1:
        lines[y].append('99999')
        lines[y].insert(0, '99999')
lines[1][1] = '0'

stack = [((1, 1), 0)]
visited = set()
visited.add((1,1))
stackSet = set()
stackSet.add((1,1))
while True:
    if len(stack) > 0:
        node, dist = stack.pop(0)
    else:
        break
    visited.add(node)
    stackSet.remove(node)
    #print(len(stack), len(visited))
    for m in range(-1, 2, 2):
        x = node[0]
        y = node[1]
        if x+m != 0 and x+m != len(lines[0])-1 and (x+m, y) not in visited and (x+m, y) not in stackSet:
            stack.append(((x+m, y), dist+int(lines[y][x+m])))
            stackSet.add((x+m, y))
        if y+m != 0 and y+m != len(lines)-1 and (x, y+m) not in visited and (x, y+m) not in stackSet:
            stack.append(((x, y+m), dist+int(lines[y+m][x])))
            stackSet.add((x, y+m))
        length = len(lines[0])-2
        if (x+m, y) == (length, length) or (x, y+m) == (length, length):
            print('HERE', dist, dist+int(lines[y][x+m]), dist+int(lines[y+m][x]))
    stack.sort(key=lambda x:x[1])
'''

linesCopy = [[[x for x in i]] for i in lines]
for i in range(5): #Value of the row for the new grid
    for j in range(5): #Value of the column for the new grid
        if not(i==0 and j==0): #Ignore the grid we already have
            newGrid = [n for n in lines]
            for y, line in enumerate(lines):
                copy = [n for n in line]
                for x, char in enumerate(line):
                    copy[x] = str((int(char) + i + j - 1)%9 + 1) #Generate the new value
                newGrid[y] = copy
            if j == 0: #If the new grid if the first in its column, add it to a new row, not the end of another row
                for y, line in enumerate(newGrid):
                    linesCopy.append(line)
            else:
                for y, line in enumerate(newGrid):
                    linesCopy[y+i*len(lines)].append(line)

for y, line in enumerate(linesCopy): #Slight formatting issue, needed to convert the lists on one line into one list. I'm not good at this
    li = []
    for lis in line:
        for ch in lis:
            li.append(ch)
    linesCopy[y] = li

lineLen = len(linesCopy[3])+1
newli = []
for line in linesCopy: #Adding buffer rows above and below
    newli.append(line)
newli.insert(0, (['99999']*(lineLen+1)))
newli.append((['99999']*(lineLen+1)))
linesCopy = newli

for y, line in enumerate(linesCopy): #Adding buffer columns left and right
    linesCopy[y] = [i for i in line]
    if y != 0 and y != len(linesCopy)-1:
        linesCopy[y].append('99999')
        linesCopy[y].insert(0, '99999')
linesCopy[1][1] = '0'

stack = [((1, 1), 0)] #Needs to hold the coordinate and its distance, so two tuples
visited = set() #Set of visited coordinates
visited.add((1,1))
stackSet = set() #Set of coordinates currently in the stack (again idk how to do this better)
stackSet.add((1,1))
while True:
    if len(stack) > 0:
        node, dist = stack.pop(0)
    else:
        break
    visited.add(node)
    stackSet.remove(node)
    #print(len(stack), len(visited))
    for m in range(-1, 2, 2): #Generates -1 and 1, which are the change in x and y for adjacent nodes
        x = node[0]
        y = node[1]
        if x+m != 0 and x+m != len(linesCopy[0])-1 and (x+m, y) not in visited and (x+m, y) not in stackSet: #Node can't be in the stack, visited already and I don't want to consider the cases that are 99999
            stack.append(((x+m, y), dist+int(linesCopy[y][x+m]))) #Add the new node to the stack, with the sum of its value and the distance travelled
            stackSet.add((x+m, y))
        if y+m != 0 and y+m != len(linesCopy)-1 and (x, y+m) not in visited and (x, y+m) not in stackSet:
            stack.append(((x, y+m), dist+int(linesCopy[y+m][x])))
            stackSet.add((x, y+m))
        length = len(linesCopy[0])-2
        if (x+m, y) == (length, length) or (x, y+m) == (length, length):
            print('HERE', dist, dist+int(linesCopy[y][x+m]), dist+int(linesCopy[y+m][x])) #If the node we add to the stack is the end node, print the values it could be (without considering cases for faster development)
    stack.sort(key=lambda x:x[1]) #Sort the stack by the second value in every position

'''
for y, line in enumerate(lines):
    if y > 0 and y < (len(lines)-1):
        copy = [i for i in line]
        for x, char in enumerate(copy):
            if x > 0 and x < (len(lines[1])-1) and not (x==1 and y==1):
                if int(lines[y-1][x]) < int(copy[x-1]):
                    copy[x] = str(int(lines[y-1][x]) + int(char))
                else:
                    copy[x] = str(int(copy[x-1]) + int(char))
        lines[y] = copy
for line in lines:
    print(line)'''
#print('\n\n\n', lines[-2][-2])        


print(f'The program took {time.perf_counter()} seconds')