
def queen_safe (board, row, col, n ):
    for c in range (col,-1,-1): 
        if board[row][c] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0 :
        if board[i][j]==1:
            return False
        i -=1
        j -=1
    i = row
    j = col
    while i < n and j >= 0 :
        if board[i][j] == 1 :
            return False 
        i += 1
        j -= 1 
    return True

def NQueens (board, col, n):
    if col>=n: 
        return True
    for i in range (n):
        if queen_safe (board, i, col, n):
            board[i][col] = 1 
            if NQueens (board, col+1, n):
                return True
            board[i][col] = 0
    return False

def make_board(n):
    board=[[0 for column in range (n)] for row in range (n)] 
    if NQueens(board, 0, n ) == True : 
        for row in range (n): 
            for column in range (n) :
                print (board[row][column], end = '') 
            print()
    else:
        print("not possible")
        
Bsize = int(input('Enter size of the board :'))
make_board(Bsize)
        