r = int(input("Enter how many row in 1st matrix:"))
c = int(input("Enter how many column in 1st matrix:"))
print("enter the values of first matrix:")
mat1 = [[int(input()) for X in range(c)]for y in range(r)]
r2 = int(input("Enter how many row in 2nd matrix:"))
c2 = int(input("Enter how many column in 2nd matrix:"))
print("enter the values of second matrix:")
mat2 = [[int(input()) for X in range(c2)]for y in range(r2)]
print('matrix1 after taking input:')
for i in range(r):
    for j in range(c):
        print(mat1[i][j], end=" ")
    print()
print('matrix2 after taking input:')
for i in range(r2):
    for j in range(c2):
        print(mat2[i][j], end=" ")
    print()

multiplication_result = [[int(0) for X in range(c2)]for y in range(r)]
if(c==r2):
    for i in range(len(mat1)):
        for j in range(len(mat2[0])): 
            for k in range(len(multiplication_result)):  
                multiplication_result[i][j]=mat1[i][k]*mat2[k][j] 
                print('Result after multiplication:')
                for item in multiplication_result:
                    print(item)     
else:
    print('multiplication not possible')


