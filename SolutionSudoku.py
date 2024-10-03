import numpy
import copy
import random

def Print_Matrix(matrix):
    for i in range(0, 9):
        for j in range(0, 9):
            print(matrix[i][j], end = ' ')
        print()

# Đọc file Test và tạo file để lưu kết quả
file = open('Result.txt', 'w')
b = numpy.load('data.npz')['data']
test_code = random.randint(0, 10000)
a = b[test_code].tolist()
Print_Matrix(a)
aa = copy.deepcopy(a)

# Khởi tạo những giá trị cần thiết
N = 9

row = [[0 for _ in range(10)] for _ in range(10)]
column = [[0 for _ in range(10)] for _ in range(10)]
square = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]

x = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]

# Xóa những số có giá trị 0 ở trong mảng những số có thể điền vào ô trống
def Delete_Number_0():
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                x[i][j] = [num for num in x[i][j] if num != 0]

# Kiểm tra xem những giá trị có thể điền có đúng hay không
def Check_Again():
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                for tmp in range(len(x[i][j])):
                    if (row[i][x[i][j][tmp]] == 1 or column[j][x[i][j][tmp]] == 1 or square[i//3][j//3][x[i][j][tmp]] == 1) and x[i][j][tmp] != 0:
                        x[i][j][tmp] = 0

# Điền vào ô chỉ còn duy nhất một số có thể điền vào
def The_Last_Free_Cell(i, j):
    if len(x[i][j]) == 1 and row[i][x[i][j][0]] == 0 and column[j][x[i][j][0]] == 0 and square[i//3][j//3][x[i][j][0]] == 0:
        if x[i][j][0] != aa[i][j]:
            return
        
        print ("1 " + str(i) + " " + str(j) + " " + str(x[i][j][0]))
        print(x[i][j])
        file.write("1 " + str(i) + " " + str(j) + " " + str(x[i][j][0]) + '\n')

        a[i][j] = x[i][j][0]
        row[i][x[i][j][0]] = 1
        column[j][x[i][j][0]] = 1
        square[i//3][j//3][x[i][j][0]] = 1

# Điền vào ô trống giá trị mà ở hàng đó duy nhất ô đang xét có thể điền được        
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
        print (x[i][j]) 
        print (colList)
        file.write("2 " + str(i) + " " + str(j) + " " + str(num) + '\n')

        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return
# Điền vào ô trống giá trị mà ở cột đó duy nhất ô đang xét có thể điền được        
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
        print (x[i][j]) 
        print (rowList)
        file.write("3 " + str(i) + " " + str(j) + " " + str(num) + '\n')

        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return

# Điền vào ô trống giá trị mà ở ô vuông đó duy nhất ô đang xét có thể điền được        
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
        if aa[i][j] != num:
            return

        print ("4 " + str(i) + " " + str(j) + " " + str(num))
        print (x[i][j]) 
        print (squareList)
        file.write("4 " + str(i) + " " + str(j) + " " + str(num) + '\n')

        a[i][j] = num
        row[i][num] = 1
        column[j][num] = 1
        square[i//3][j//3][num] = 1
        return    


# Giải ma trận Sudoku bằng phương pháp sinh thông thường
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

# Kiểm tra các cột, hàng, ô vuông cho phù hợp
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

# Xem xét những ô trống có thể điền được những giá trị gì
for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] == 0:
            for value in range(1, 10):
                if row[i][value] != 1 and column[j][value] != 1 and square[i//3][j//3][value] != 1:
                    x[i][j].append(value)

# Solution of Sudoku
if (solveSudoku(aa, 0, 0)):
    Print_Matrix(aa)
else:
    print("no solution  exists ")

print()


# Giải Sudoku theo từng bước giải
for count in range(0, 100):
    Check_Again()
    Delete_Number_0()
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                The_Last_Free_Cell(i, j)
    
    Check_Again()
    Delete_Number_0()
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Row(i, j)

    Check_Again()
    Delete_Number_0()
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Column(i, j)

    Check_Again()
    Delete_Number_0()
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                The_Last_Remaining_Cell_In_Square(i, j)

# In đáp án cuối cùng sau khi hoàn thành giải theo từng bước
Print_Matrix(a)

for i in range(0, 9):
    for j in range(0, 9):
        if a[i][j] == 0:
            print(i, j, x[i][j])

file.close()