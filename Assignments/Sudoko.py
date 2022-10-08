#NAME: Kondrolla Dinesh Reddy
#ROLL NO: 2020BTechCSE040


M = 9

grid = [[9,7,0,6,0,0,0,0,0],
        [2,0,1,0,3,0,0,0,0],
        [0,0,0,0,0,0,6,4,0],
        [0,0,0,5,0,0,0,0,4],
        [0,8,6,3,0,2,0,0,9],
        [0,0,0,1,0,0,0,3,0],
        [5,0,0,0,0,0,7,0,0],
        [0,2,0,0,5,0,0,9,0],
        [0,0,0,7,0,0,0,6,2]]

def solve(grid, row, col, num):
    for x in range(M):
        if grid[row][x] == num:
            return False
             
    for x in range(M):
        if grid[x][col] == num:
            return False
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
       return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 

def print_puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
 
if (Suduko(grid, 0, 0)):
    print_puzzle(grid)
else:
    print("Solution does not exist:(")
