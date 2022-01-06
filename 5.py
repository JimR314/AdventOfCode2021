import os
import time
import math

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '5.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

grid = [('.' * 1100) for i in range(1100)]


'''
for i,line in enumerate(lines):
    coord1, coord2 = line.split(' -> ')
    x1, y1 = coord1.split(',')
    x2, y2 = coord2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if y1 == y2:
        for x,char in enumerate(grid[y1]):
            if (x >= x1 and x <= x2) or (x <= x1 and x >= x2):
                if char == '.':
                    grid[y1] = grid[y1][:x] + '1' + grid[y1][x+1:]
                else:
                    grid[y1] = grid[y1][:x] + str(int(grid[y1][x])+1) + grid[y1][x+1:]
    if x1 == x2:
        for x,line in enumerate(grid):
            if (x >= y1 and x <= y2) or (x <= y1 and x >= y2):
                if line[x1] == '.':
                    grid[x] = grid[x][:x1] + '1' + grid[x][x1+1:]
                else:
                    grid[x] = grid[x][:x1] + str(int(line[x1])+1) + grid[x][x1+1:]

for row in grid:
    for char in row:
        if char != '.' and char != '1':
            total += 1
print(total)
#for line in grid:
#    print(line)
'''

for i,line in enumerate(lines):
    coord1, coord2 = line.split(' -> ')
    x1, y1 = coord1.split(',')
    x2, y2 = coord2.split(',')
    x1 = int(x1) #Me forgetting how to do this quickly
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if y1 == y2: #Horizontal line
        for x,char in enumerate(grid[y1]):
            if (x >= x1 and x <= x2) or (x <= x1 and x >= x2):
                if char == '.':
                    grid[y1] = grid[y1][:x] + '1' + grid[y1][x+1:]
                else:
                    grid[y1] = grid[y1][:x] + str(int(grid[y1][x])+1) + grid[y1][x+1:]
    elif x1 == x2:#Vertical line
        for x,line in enumerate(grid):
            if (x >= y1 and x <= y2) or (x <= y1 and x >= y2):
                if line[x1] == '.':
                    grid[x] = grid[x][:x1] + '1' + grid[x][x1+1:]
                else:
                    grid[x] = grid[x][:x1] + str(int(line[x1])+1) + grid[x][x1+1:]
    elif abs(x2-x1) == abs(y2-y1): #Diagonal line
        counter = x1
        points = [] #A list that will store all the points inbetween
        if x1 > x2 and y1 > y2: #I decided it was easiest to generate every point between two than to go about it any other way
            while counter >= x2: #These 4 while loops basically account for (North|South)(East|West)
                points.append((x1, y1))
                x1 -= 1
                y1 -= 1
                counter -= 1
        elif x1 > x2 and y1 < y2:
            while counter >= x2:
                points.append((x1, y1))
                x1 -= 1
                y1 += 1
                counter -= 1
        elif x1 < x2 and y1 > y2:
            while counter <= x2:
                points.append((x1, y1))
                x1 += 1
                y1 -= 1
                counter += 1
        elif x1 < x2 and y1 < y2:
            while counter <= x2:
                points.append((x1, y1))
                x1 += 1
                y1 += 1
                counter += 1
        for x, y in points: #Literally just iterate through the generated point, and change the values in the grid    
            if grid[y][x] == '.':
                grid[y] = grid[y][:x] + '1' + grid[y][x+1:]
            else:
                grid[y] = grid[y][:x] + str(int(grid[y][x])+1) + grid[y][x+1:]



for row in grid:
    for char in row:
        if char != '.' and char != '1':
            total += 1
print(total)

print(f'The program took {time.perf_counter() - start:0.4f} seconds')