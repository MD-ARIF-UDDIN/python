r = int(input("Enter how many row:"))
c = int(input("Enter how many column:"))
print("enter the values of first matrix:")
mat1 = [[int(input()) for X in range(c)]for y in range(r)]
print("enter the values of second matrix:")
mat2 = [[int(input()) for X in range(c)]for y in range(r)]
print('matrix1 after taking input:')
for i in range(r):
    for j in range(c):
        print(mat1[i][j], end=" ")
    print()
print('matrix2 after taking input:')
for i in range(r):
    for j in range(c):
        print(mat2[i][j], end=" ")
    print()

addition_result = [[int(0) for X in range(c)]for y in range(r)]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        addition_result[i][j] = mat1[i][j] + mat2[i][j]

print('Result after addition:')
for item in addition_result:
    print(item)
