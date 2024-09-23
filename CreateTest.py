import numpy as np
from random import sample

base  = 3
side  = base*base
squares = side*side
empties = squares * 5//9

data = []
test = []

for i in range(1, 10000):
    tmp = []
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    numSize = len(str(side))
    for line in board:
        tmp.append(*(f"{n or '.':{numSize}} " for n in line))

    test.append(tmp)

test_np = np.array(test)
np.savez_compressed('D:/02_Tùng Dương_12T2/python code/ProjectPythonStudy/test.npz', data = test_np)