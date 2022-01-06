import os
import time

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '1.txt'), 'r').readlines()
numbers = []
for line in f:
    numbers.append(int(line[:-1]))

#Part 1
'''
total = 0
counter = -999
for num in numbers:
    if counter == -999:
        counter = num
    else:
        if num > counter:
            total += 1
            counter = num
        else:
            counter = num
print(total)'''

#Part 2
'''
total = 0
counter1 = numbers[2]
counter2 = numbers[1]
counter3 = numbers[0]
tot = counter1+counter2+counter3
for num in range(3, len(numbers)):
    print(tot, counter1, counter2, counter3)
    counter3 = counter2
    counter2 = counter1
    counter1 = numbers[num]
    if tot < counter1+counter2+counter3:
        total += 1
    tot = counter1+counter2+counter3
print(total)'''

#Part 2 but dense
#print(sum([1 for i, num in enumerate(numbers[3:]) if num > numbers[i]]))
print(f"The code took {time.perf_counter() - start:0.4f} seconds")