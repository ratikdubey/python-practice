r1 = int(input('Enter number of rows for A: '))
c1 = int(input('Enter number of columns for A: '))

A = [[0 for row in range(r1)]for column in range(c1)]

# Matrix A
print('Original Matrix:', A)
for i in range(0,r1):
    for j in range(0,c1):

        print('Enter value for matrix A', i+1,j+1, ':')

        val = int(input())

        A[i][j] = val

print('Original Matrix A')
for i in range(0,r1):
    for j in range(0,c1):
        print(A[i][j], end = ' ')
    print()

print()

# Transpose of a matrix

