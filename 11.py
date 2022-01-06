import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '11.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0


lineLen = len(lines[3])+1
newli = []
for line in lines:
    line = '.' + line
    line += '.'
    newli.append(line)
newli.insert(0, ('.'*(lineLen+1)))
newli.append(('.'*(lineLen+1)))
lines = newli
#print(lines)

def changeChar(x, y):
    char = lines[y][x]
    if char != '9' and char != '.' and char != '*':
        return str(int(char) + 1)
    elif char == '9' or char == '*':
        return '*'
    else:
        return char

for i in range(10000):
    for y, line in enumerate(lines): #Increment every value by one or convert a 9 into a flash *
        if y != 0 and y != lineLen:
            newLine = '.'
            for x, char in enumerate(line):
                if x != 0 and x != lineLen:
                    if char != '9':
                        newLine += str(int(char) + 1)
                    else:
                        newLine += '*'
            newLine += '.'
            lines[y] = newLine
    setToZero = [] #List of values that I must keep at 0 if they've flashed this turn
    thisTurn = 0 #Part 2: number of flashes this turn
    while True:
        changed = 0 #Keeps track to see if anything has flashed, if so, i need to check things again
        for y, line in enumerate(lines):
            if y != 0 and y != lineLen:
                for x, char in enumerate(line):
                    if x != 0 and x != lineLen and char == '*':
                        setToZero.append((x, y)) #Adds anything that will flash to the set
        for y, line in enumerate(lines): #Main loop, that adds one to adjacent cells to ones that flash
            if y != 0 and y != lineLen:
                for x, char in enumerate(line):
                    if x != 0 and x != lineLen and char == '*': #I surrounded the grid in dots so i'm avoiding those
                        total += 1
                        thisTurn += 1
                        changed += 1
                        if (x, y) not in setToZero: #The character is a * so it shouldn't go beyond 0
                            setToZero.append((x, y))
                        for m in range(-1, 2): #Getting the adjacent cells
                            for n in range(-1, 2):
                                if not (m==0 and n==0):
                                    if lines[y+m][x+n] != '*': #If an adjacent cell is already going to flash, do nothing, otherwise increment
                                        lines[y+m] = lines[y+m][:x+n] + changeChar(x+n, y+m) + lines[y+m][x+n+1:]
        for y, line in enumerate(lines): #Change all the octopuses that flashed to a 0
            copy = ''
            for x, char in enumerate(line):
                if (x, y) in setToZero:
                    copy += '0'
                else:
                    copy += char
            lines[y] = copy
        if changed == 0: #If nothing changed, i can end this step and move onto the next one
            break
    if thisTurn == 100: #10x10 grid, so if 100 of them flashed, I'm finished
        print(i+1)
        break

#Part 1 code
#for line in lines:
#    print(line)
#print(total)

print(f'The program took {time.perf_counter() - start:0.4f} seconds')