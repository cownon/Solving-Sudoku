import numpy as np
from random import sample

base  = 3
side  = base*base
squares = side*side
empties = squares * 5//9

data = []
test = []

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s, len(s)) 

for i in range(1, 10000):
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    tmp = []
    for line in board: 
        tmp.append(line)

    data.append(tmp)

    tmp_test = []
    for p in sample(range(squares), empties):
        board[p//side][p%side] = 0

    numSize = len(str(side))
    for line in board:
        tmp_test.append([int(n) if n else 0 for n in line])

    test.append(tmp_test)


data_np = np.array(data)
np.savez_compressed('D:/02_Tùng Dương_12T2/python code/ProjectPythonStudy/data.npz', data = data_np)

test_np = np.array(test)
np.savez_compressed('D:/02_Tùng Dương_12T2/python code/ProjectPythonStudy/test.npz', test = test_np)