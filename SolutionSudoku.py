import numpy
import copy

b = numpy.load('data.npz')['data']
print(b[3])

a = b[3].tolist()

aa = copy.deepcopy(a)

# a = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#     [5, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 8, 7, 0, 0, 0, 0, 3, 1],
#     [0, 0, 3, 0, 1, 0, 0, 8, 0],
#     [9, 0, 0, 8, 6, 3, 0, 0, 5],
#     [0, 5, 0, 0, 9, 0, 6, 0, 0],
#     [1, 3, 0, 0, 0, 0, 2, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 7, 4],
#     [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# a = [[4, 0, 1, 5, 0, 9, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 4, 8],
#      [3, 0, 6, 0, 0, 0, 0, 2, 0],
#      [0, 3, 9, 0, 7, 0, 0, 0, 0],
#      [2, 0, 0, 0, 0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 5, 0, 9, 0, 2],
#      [8, 7, 0, 1, 0, 0, 0, 0, 0],
#      [0, 5, 0, 3, 4, 0, 7, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 6]]

N = 9

row = [[0 for _ in range(10)] for _ in range(10)]
column = [[0 for _ in range(10)] for _ in range(10)]
square = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]

x = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]

def Delete_Number_0():
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                x[i][j] = [num for num in x[i][j] if num != 0]

def Check_Again():
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                for tmp in range(len(x[i][j])):
                    if (row[i][x[i][j][tmp]] == 1 or column[j][x[i][j][tmp]] == 1 or square[i//3][j//3][x[i][j][tmp]] == 1) and x[i][j][tmp] != 0:
                        x[i][j][tmp] = 0
    return


def The_Last_Free_Cell(i, j):
    if len(x[i][j]) == 1 and row[i][x[i][j][0]] == 1 and column[j][x[i][j][0]] == 1 and square[i//3][j//3][x[i][j][0]] == 1:
        print ("1 " + str(i) + " " + str(j) + " " + str(x[i][j][0]))
        print(x[i][j])
        a[i][j] = x[i][j][0]
        row[i][x[i][j][0]] = 1
        column[j][x[i][j][0]] = 1
        square[i//3][j//3][x[i][j][0]] = 1
        
def The_Last_Remaining_Cell_In_Row(i, j):
    colList = []
    colList.clear()

    for col in range(0, 9):
        if a[i][col] == 0 and col != j:
            colList.extend(x[i][col])
    
    for num in x[i][j]:
        if num in colList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i//3][j//3][num] == 1:
            continue
        if len(colList) == 0:
            return
        if aa[i][j] != num:
            return
        
        print ("2 " + str(i) + " " + str(j) + " " + str(num))
        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return

def The_Last_Remaining_Cell_In_Column(i, j):
    rowList = []
    rowList.clear()

    for r in range(0, 9):
        if a[r][j] == 0 and r != i:
            rowList.extend(x[r][j])

    for num in x[i][j]:
        if num in rowList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i//3][j//3][num] == 1:
            continue
        if len(rowList) == 0:
            return
        if aa[i][j] != num:
            return
        
        print ("3 " + str(i) + " " + str(j) + " " + str(num))
        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return

def The_Last_Remaining_Cell_In_Square(i, j):
    squareList = []
    squareList.clear()

    for r in range(i//3 * 3, i//3 * 3 + 3):
        for col in range(j//3 * 3, j//3 * 3 + 3):
            if a[r][col] == 0 and r != i and col != j:
                squareList.extend(x[r][col])
    
    for num in x[i][j]:
        if num in squareList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i//3][j//3][num] == 1:
            continue
        if len(squareList) == 0:
            return
        if aa[i][i] != num:
            return

        print ("4 " + str(i) + " " + str(j) + " " + str(num))
        print (x[i][j]) 
        print (squareList)
        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return    

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

for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] != 0:
            row[i][a[i][j]] = 1 
        else:
            row[i][a[i][j]] = 0

for j in range(0, 9):
    for i in range(0, 9):
        if a[i][j] != 0:
            column[j][a[i][j]] = 1
        else:
            column[j][a[i][j]] = 0

for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] != 0:
            square[i//3][j//3][a[i][j]] = 1
        else:
            square[i//3][j//3][a[i][j]] = 0

for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] == 0:
            for value in range(0, 10):
                if row[i][value] != 1 and column[j][value] != 1 and square[i//3][j//3][value] != 1:
                    x[i][j].append(value)

if (solveSudoku(aa, 0, 0)):
    for i in range(0, 9):
        for j in range(0, 9):
            print(aa[i][j], end = ' ')
        print()
else:
    print("no solution  exists ")

print()

for count in range(0, 200):
    Check_Again()
    Delete_Number_0()
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                The_Last_Free_Cell(i, j)
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Row(i, j)
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Column(i, j)
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Square(i, j)

for i in range(0, 9):
    for j in range(0, 9):
        print(a[i][j], end = ' ')
    print()

for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] == 0:
            print(i, j, x[i][j])