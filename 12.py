import math
import os
import time
from collections import *

import aoctools as at

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '12.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])
print('\n')
total = 0

cons = []
visited = []
twice = False
for y, line in enumerate(lines):
    s, e = line.split('-')
    cons.append((s, e))
def route(node, visited, extra, twice):
    #print(node, extra)
    if node == 'end':
        #print(node, extra)
        return 1
    else:
        if node[0].lower() == node[0]: #Don't visit lower case ones more than once/twice
            if node in visited:
                twice = True 
            visited.append(node)    
        extra.append(node)
        adj = []
        for con in cons:
            if con[0] == node and con[1] != 'start':
                if twice:
                    if con[1] not in visited:
                        adj.append(con[1])
                else:
                    adj.append(con[1])
            elif con[1] == node and con[0] != 'start':
                if twice:
                    if con[0] not in visited:
                        adj.append(con[0])
                else:
                    adj.append(con[0])
        
        #print(node, adj, visited)
        check = twice
        tot = sum([route(a, [i for i in visited], [i for i in extra], check) for a in adj])
        return tot
print(route('start', [], [], twice))
        

print(f'The program took {time.perf_counter() - start:0.4f} seconds\n')