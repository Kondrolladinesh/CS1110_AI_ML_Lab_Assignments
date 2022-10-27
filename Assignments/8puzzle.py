import numpy as np
#initialmatrix=np.array([['2','8','3'],['1','6','4'],['7',' ','5']])
#finalmatrix=np.array([['1','2','3'],['8',' ','4'],['7','6','5']])

initialmatrix = np.array([['3','7','6'],['5','1','2'],['4','8',' ']])
finalmatrix = np.array([['5','3','6'],['7',' ','2'],['4','1','8']])
box=initialmatrix
list1 = []
list2 = []

def make_order(puzzle):
    for i in range(len(puzzle)) : 
        for j in range(len(puzzle[i])) : 
            if(puzzle[i][j]!=' '):
                list1.append(puzzle[i][j])
            else:
                list2.append(i)
                list2.append(j)
    return list1

def check_solvable():
    l = make_order(initialmatrix)
    Tsum=0
    for i in range(len(l)):#
        count=0
        for j in range(i,len(l)):
            if(l[i]>l[j]):
                count +=1
        Tsum += count
    print("Inversion Rule value: ",Tsum)
    print(" ")
    if(Tsum%2==0):
        print("The 8-Puzzle is solvable\n")
        return True
    else:
        print("The 8-puzzle is not solvable")
        return False
                
def Moves(i,j):
    return [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]

def check_isSafe(i,j):
    return i>=0 and i<3 and j>=0 and j<3

def find_Manhattan(box):
    sum=0
    for i in range(3):
        for j in range(3):
            if box[i][j]!=' ':
                sum = sum+abs(i-np.where(finalmatrix==box[i][j])[0][0])+abs(j-np.where(finalmatrix==box[i][j])[1][0])
    return sum
            

def solve(blankR, blankC):
    global box
    if np.array_equal(box,finalmatrix):
        return
    
    manhattanDistance=[]
    for move in Moves(blankR,blankC):
        if check_isSafe(move[0],move[1]):
            box[move[0]][move[1]],box[blankR][blankC]=box[blankR][blankC],box[move[0]][move[1]]
            manhattanDistance.append([find_Manhattan(box),box.copy(),move[0],move[1]])
            box[move[0]][move[1]],box[blankR][blankC]=box[blankR][blankC],box[move[0]][move[1]]
    
    manhattanDistance.sort(key = lambda manhattanDistance: manhattanDistance[0])
    box=manhattanDistance[0][1]
    print(box)
    print()
    solve(manhattanDistance[0][2],manhattanDistance[0][3])

def main():
    if(check_solvable()):
        print("STEPS TO SOLVE\n")
        solve(list2[0],list2[1])
    else:
        print(" ")
main()
    

