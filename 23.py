import collections
import os
import time
from collections import *
import itertools
import copy

import aoctools as at

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '23.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

print('\n')

total = 0

#2000+3000+10+6+5000+700+20+500+30+50+3+3

#############
#...........#
###C#B#A#D###
  #B#C#D#A#
  #########

#min:
#10000+600+600+50+50+7+9
#7+9+5000+5000+700+20+500+30+50+6

#############
#...........#
###C#B#A#D###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#D#A#
  #########

#############
#...........#
###C#B#A#D###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#D#A#
  #########

  
#############
#AA.......AA#
###.#.#C#.###
  #D#B#C#.#
  #D#B#C#D#
  #B#B#C#D#
  #########

#############
#...........#
###C#B#A#D###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#D#A#
  #########
#7+40+50+800+80+700+50+60+8+7000+500+700+70+4000+4+700+5+7000+8000+600+20000+70+5+5+9+9
# = 50472

#############
#AA.......AA#
###.#B#C#D###
  #.#B#C#D#
  #.#B#C#D#
  #.#B#C#D#
  #########
#7+40+700+40+700+50+60+60+8+7000+500+600+4000+4+700+5+7000+8000+600+10000+10000+70+5+5+9+9
# = 50172
#49532


#min:
#7000+9000+20000+900+900+600+500+150+60+70+9+10+10+11
#39220

grid = []
for line in lines:
    grid.append([i for i in line])

print(grid)
#while True:
#    total = 0


print(f'The program took {time.perf_counter()} seconds')