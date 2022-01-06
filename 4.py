import os
import time
import math

start = time.perf_counter()

dirname = os.path.dirname(__file__)
f = open(os.path.join(dirname, '4.txt'), 'r').readlines()
lines = []
for line in f:
    lines.append(line[:-1])

total = 0

balls = []
boards = []
board = []
for i, line in enumerate(lines):
    if i == 0:
        balls =line.split(',')
    elif line == '':
        board = []
    else:
        board.append(line.split())
    if len(board) == 5:
        boards.append(board)


def findScore(board, ball):
    totalU = 0
    for row in board:
        for item in row:
            if item not in called:
                totalU += int(item)
    return (totalU, ball, totalU*int(ball))

called = []
calculate = False
for ball in balls:
    boardsCopy = [board for board in boards]
    called.append(ball)
    if calculate:
        print(findScore(boards[0], ball))
        break
    for board in boardsCopy:
        remove = False
        repeat = True
        for row in board:
            every = True
            for number in row:
                if number not in called:
                    every = False
            if every:
                remove = True
                repeat = False
                break
            if not repeat:
                break
        for col in range(5):
            every = True
            for row in range(5):
                if board[row][col] not in called:
                    every = False
            if every:
                #print(board, called)
                remove = True
                repeat = False
                break
            if not repeat:
                break
        if remove:
            boardsCopy.remove(board)
    boards = boardsCopy
    if len(boards) == 1:
        calculate = True

print(f'The program took {time.perf_counter() - start:0.4f} seconds')