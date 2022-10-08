import numpy as np
print("You are playing magic square")
print()
n = int(input("Enter a number 'n' for n*n: "))
array = [[0 for i in range(n)] for j in range(n)]
arr = np.array(array)
row = 0
col = n//2    
num = 1
arr[row,col] = num

print("Before solving Magic square\n",arr)
constant = int(n*(n**2 + 1)/2)
print("The value of constant : ",constant)    
while(num<n*n):
    num +=1
    row -= 1
    col += 1
    if(row == -1 and col == n):
        row += 2
        col -= 1
    elif(col == n):
        col = 0
    elif(row == -1):
        row = n-1
    elif(arr[row,col] != 0):
        row += 2
        col -= 1
    arr[row,col] = num

print()
print("After Solving the magic square\n", arr)