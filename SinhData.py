import numpy as np
from random import sample
import copy

base  = 3
side  = base*base
squares = side*side
empties = squares * 5//9
N = 9

data = []

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s, len(s)) 

def isSafe(aa, row, col, num):
    for x in range(9):
        if aa[row][x] == num:
            return False

    for x in range(9):
        if aa[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if aa[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(aa, row, col):
    if (row == N - 1 and col == N):
        return True
      
    if col == N:
        row += 1
        col = 0

    if aa[row][col] > 0:
        return solveSudoku(aa, row, col + 1)
    for num in range(1, N + 1, 1):
        if isSafe(aa, row, col, num):         
            aa[row][col] = num
            if solveSudoku(aa, row, col + 1):
                return True

        aa[row][col] = 0
    return False

for i in range(1, 10000):
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    tmp = []
    for p in sample(range(squares), empties):
        board[p//side][p%side] = 0
    
    for line in board:
        tmp.append(line)

    tmp_test = copy.deepcopy(tmp)

    if (solveSudoku(tmp, 0, 0)):
        data.append(tmp_test)

data_np = np.array(data)
np.savez_compressed('D:/02_Tùng Dương_12T2/python code/ProjectPythonStudy/data.npz', data = data_np)
print(len(data))