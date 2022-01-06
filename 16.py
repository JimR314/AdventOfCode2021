import math
import os
import time
from collections import *

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '16.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

scale = 16

def addV(bits, start, end): #Find the version number of a packet
    return int(bits[start:end], 2)

#def split(bits): #Split some bits into their packets, and return the packets
#    li = []
#    for i, bit in enumerate(bits):

def findEnd(bits): #Return the contents of the first packet
    i = 0
    while True:
        if bits[i] == '0':
            return bits[:(i+5)]
        else:
            i += 5

def divide(bits): #Split some bits into their packets, and return the packets
    #print(bits)
    li = []
    if bits[3:6] == '100':
        return [bits[:6]+findEnd(bits[6:])] #No more version numbers, so end recursion
    elif len(bits) > 7:
        print(bits)
        if bits[6] == '0':
            length = int(bits[7:22], 2)
            print(length, 'hi')
            count = 0
            while count < length:
                #print('H', bits)
                #print('HI', bits[22:])
                #print('HELLO', bits[22+count:])
                if bits[25+count:28+count] == '100':                
                    packet = bits[22+count:28+count]+findEnd(bits[28+count:28+count+length])
                    li.append(packet)
                    count += len(packet)
                    #print(packet)
                else:
                    time.sleep(0.01)
                    packets = divide(bits[22+count:22+count+length])
                    #print(packets, li)
                    for x, packet in enumerate(packets):
                        li.append(packet)
                        if x != 0:
                            count += len(packet)
                        if x == 0:
                            if packet[3:6] != '100':
                                count += 22 if packet[7]=='0' else 18
                            else:
                                count += len(packet)
                    #print(count, length)
            #print([bits] + li)
            output = [bits]
            for x in li:
                if x not in output:
                    output.append(x)
            #return output
            return [bits] + li
        else:
            length = int(bits[7:18], 2) #Number of packets to come
            print(length)
            count = 0
            for i in range(length):
                print(count)
                #print(bits[18+count:])
                #print(bits[21+count:24+count]) 0011001110010000010010011001111011010111000010011110011011101011010010011010010111001100010010100011101000111
                if bits[21+count:24+count] == '100':
                    print(count, bits[:count+18+1])
                    packet = bits[18+count:24+count] + findEnd(bits[24+count:])
                    count += len(packet)
                    li.append(packet)
                    print(count)
                else:
                    print(count, 'hel')
                    lis = divide(bits[18+count:])
                    #print(lis)
                    for w, x in enumerate(lis):
                        li.append(x)
                        if w != 0:
                            #li.append(x)
                            count += len(x)
                        if w == 0:
                            if x[3:6] != '100':
                                count += 22 if x[6]=='0' else 18
                            else:
                                count += len(x)
                    #print(bits)
            print(li)
            output = [bits]
            for x in li:
                if x not in output:
                    output.append(x)
            #return output
            return [bits] + li
    else:
        return []
                    

for y, line in enumerate(lines):
    bits = str(bin(int(line, scale))[2:].zfill(4*len(line)))
    #print(bits, '\n')
    li = divide(bits)
for packet in li:
    total += int(packet[:3], 2)
print(total, li)
    #for x, char in enumerate(bits):
    #    total += addV(bits, 0, 3)

        
        

print(f'The program took {time.perf_counter()} seconds')