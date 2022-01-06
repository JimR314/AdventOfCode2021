import math
import os
import time
from collections import *

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '14.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')
total = 0

ch = lines[0]
d = ch
start = False
pairs = {}
for line in lines:
    if line == '':
        start = True
    elif start:
        n = line.split(' -> ')
        pairs[n[0]] = n[1]


alphabet = [chr(i+65) for i in range(26)]

#Part 1:
'''for i in range(15):
    copy = ''
    for x, char in enumerate(ch):
        copy += char
        if x != (len(ch) - 1):
            if (char+ch[x+1]) in pairs:
                copy += pairs[(char+ch[x+1])]
    ch = copy
    
for c in alphabet:
    if c in d:
        print(c, ch.count(c))'''

#Part 2 below:
counts = defaultdict(lambda: 0)

for x, char in enumerate(ch): #Turn the string into a dictionary of the pairs for the iterations
    if x != (len(ch) - 1):
        if (char+ch[x+1]) in pairs:
            counts[(char+ch[x+1])] += 1

def findPairCount(dict): #Given a dictionary of elemental pairs, return a new dictionary after one round of reactions
    copy = defaultdict(lambda: 0)
    for pair in dict:
        copy[pair] = dict[pair] #Wasn't sure how to generate a copy of a dictionary lmao
    for pair in dict:
        if dict[pair] != 0:
            copy[pair] -= dict[pair] #Forgot for a while that if you have multiple of the same pair, they all react
            new = pairs[pair]
            s1 = pair[0] + new #New elemental pair one
            s2 = new + pair[1] #New elemental pair one
            copy[s1] += dict[pair] #Add each new pair the number of time the source pair occurred
            copy[s2] += dict[pair]
    return copy

alpha = defaultdict(lambda: 0) #Will store how many times every letter occurs
for i in range(40):
    counts = findPairCount(counts)
for i, pair in enumerate(counts):
    for c in pair:
        alpha[c] += counts[pair]
alpha[d[0]] += 1 #Because it goes through every pair, every letter is double counted apart from the first and last
alpha[d[-1]] += 1 #d[n] is just the nth letter in the starting polymer
mi = 99999999999999999999
ma = 0
for c in alpha:
    alpha[c] /= 2 #Every letter is double counted
    total += alpha[c]
for c in alpha: #Find the maximum and minimum
    if alpha[c] > ma:
        ma = alpha[c]
    if alpha[c] < mi:
        mi = alpha[c]
print(ma, mi, ma-mi)

print(f'The program took {time.perf_counter()} seconds')