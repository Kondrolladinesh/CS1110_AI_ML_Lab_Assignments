import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
player = 1        
Win = 1    
Draw = -1    
Running = 0    
Stop = 1        
Game = Running    
Mark = 'X'    
   
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
     
def CheckWin():    
    global Game    
    #H  
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #V   
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #D    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #MT   
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running  
    
def AIStep(mark,Mark):    
    #global Game
    if(board[5] ==' '):
        return(5)

    elif(board[1] == board[2] and board[1] == Mark and board[3] == ' '):    
        return(3) 
    elif(board[2] == board[3] and board[2] == Mark and board[1] == ' '):    
        return(1)
    elif(board[3] == board[1] and board[3] == Mark and board[2] == ' '):    
        return(2)
    elif(board[4] == board[5] and board[4] == Mark and board[6] == ' '):    
        return(6)
    elif(board[5] == board[6] and board[5] == Mark and board[4] == ' '):    
        return(4)
    elif(board[6] == board[4] and board[6] == Mark and board[5] == ' '):    
        return(5)
    elif(board[7] == board[8] and board[7] == Mark and board[9] == ' '):    
        return(9)
    elif(board[8] == board[9] and board[8] == Mark and board[7] == ' '):    
        return(7)
    elif(board[9] == board[7] and board[9] == Mark and board[8] == ' '):    
        return(8)
    #v
    elif(board[1] == board[4] and board[1] == Mark and board[7] == ' '):    
        return(7)
    elif(board[4] == board[7] and board[4] == Mark and board[1] == ' '):    
        return(1)
    elif(board[7] == board[1] and board[7] == Mark and board[4] == ' '):    
        return(4)
    elif(board[2] == board[5] and board[2] == Mark and board[8] == ' '):    
        return(8)
    elif(board[5] == board[8] and board[5] == Mark and board[2] == ' '):    
        return(2)
    elif(board[8] == board[2] and board[8] == Mark and board[5] == ' '):    
        return(5)
    elif(board[3] == board[6] and board[3] == Mark and board[9] == ' '):    
        return(9)
    elif(board[6] == board[9] and board[6] == Mark and board[3] == ' '):    
        return(3)
    elif(board[9] == board[3] and board[9] == Mark and board[6] == ' '):    
        return(6)
    #D
    elif(board[1] == board[5] and board[1] == Mark and board[9] == ' '):    
        return(9)
    elif(board[5] == board[9] and board[5] == Mark and board[1] == ' '):    
        return(1)
    elif(board[9] == board[1] and board[9] == Mark and board[5] == ' '):    
        return(5)
    elif(board[3] == board[5] and board[3] == Mark and board[7] == ' '):    
        return(7)
    elif(board[5] == board[7] and board[5] == Mark and board[3] == ' '):    
        return(3)
    elif(board[7] == board[3] and board[7] == Mark and board[5] == ' '):    
        return(5)
    

    #H  
    elif(board[1] == board[2] and board[1] == mark and board[3] == ' '):    
        return(3) 
    elif(board[2] == board[3] and board[2] == mark and board[1] == ' '):    
        return(1)
    elif(board[3] == board[1] and board[3] == mark and board[2] == ' '):    
        return(2)
    elif(board[4] == board[5] and board[4] == mark and board[6] == ' '):    
        return(6)
    elif(board[5] == board[6] and board[5] == mark and board[4] == ' '):    
        return(4)
    elif(board[6] == board[4] and board[6] == mark and board[5] == ' '):    
        return(5)
    elif(board[7] == board[8] and board[7] == mark and board[9] == ' '):    
        return(9)
    elif(board[8] == board[9] and board[8] == mark and board[7] == ' '):    
        return(7)
    elif(board[9] == board[7] and board[9] == mark and board[8] == ' '):    
        return(8)
    #v
    elif(board[1] == board[4] and board[1] == mark and board[7] == ' '):    
        return(7)
    elif(board[4] == board[7] and board[4] == mark and board[1] == ' '):    
        return(1)
    elif(board[7] == board[1] and board[7] == mark and board[4] == ' '):    
        return(4)
    elif(board[2] == board[5] and board[2] == mark and board[8] == ' '):    
        return(8)
    elif(board[5] == board[8] and board[5] == mark and board[2] == ' '):    
        return(2)
    elif(board[8] == board[2] and board[8] == mark and board[5] == ' '):    
        return(5)
    elif(board[3] == board[6] and board[3] == mark and board[9] == ' '):    
        return(9)
    elif(board[6] == board[9] and board[6] == mark and board[3] == ' '):    
        return(3)
    elif(board[9] == board[3] and board[9] == mark and board[6] == ' '):    
        return(6)
    #D
    elif(board[1] == board[5] and board[1] == mark and board[9] == ' '):    
        return(9)
    elif(board[5] == board[9] and board[5] == mark and board[1] == ' '):    
        return(1)
    elif(board[9] == board[1] and board[9] == mark and board[5] == ' '):    
        return(5)
    elif(board[3] == board[5] and board[3] == mark and board[7] == ' '):    
        return(7)
    elif(board[5] == board[7] and board[5] == mark and board[3] == ' '):    
        return(3)
    elif(board[7] == board[3] and board[7] == mark and board[5] == ' '):    
        return(5)
    
    elif(board[1] ==' '):
        return(1)
    elif(board[2] ==' '):
        return(2)
    elif(board[3] ==' '):
        return(3)
    elif(board[4] ==' '):
        return(4)
    elif(board[6] ==' '):
        return(6)
    elif(board[7] ==' '):
        return(7)
    elif(board[8] ==' '):
        return(8)
    elif(board[9] ==' '):
        return(9)
        
print("Player 1 Vs Player 2\n")      
playerC = input("Enter which one do you want to choose('x' or ' o'):")
print("Loading Please Wait...")    
time.sleep(2)      
while(Game == Running):    
    DrawBoard()
    print('-'*60)  
    if(playerC == 'x'or playerC == 'X' ):
        if(player % 2 != 0):
            print("Player X's chance") 
            choice = int(input("Enter the position between [1-9] where you want to mark : "))
            Mark = 'X' 
        else:    
            print("Player O's chance")    
            mark = 'X'
            Mark = 'O'
            choice = AIStep(mark,Mark)
            time.sleep(2)
    else:
        if(player % 2 == 0):
            print("Player X's chance")    
            mark = 'O' 
            Mark = 'X'
            choice = AIStep(mark,Mark)
            time.sleep(2)
        else:
            print("Player O's chance")   
            choice = int(input("Enter the position between [1-9] where you want to mark : "))
            Mark = 'O'      
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()
    else:
        print()
        print("Alert: 'Enter the correct position'\n")
  
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")
        

    