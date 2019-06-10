from array import *

r1 = int(input('Enter number of rows for A: '))
c1 = int(input('Enter number of columns for A: '))

r2 = int(input('Enter number of rows for B: '))
c2 = int(input('Enter number of columns for B: '))

A = [[0 for row in range(r1)]for column in range(c1)]
B = [[0 for row in range(r2)]for column in range(c2)]
C = [[0 for row in range(r1)]for column in range(c2)]

print('Original Matrix:', A)

# Matrix A

for i in range(0,r1):
    for j in range(0,c1):

        print('Enter value for matrix A', i+1,j+1, ':')

        val = int(input())

        A[i][j] = val


for i in range(0,r2):
    for j in range(0,c2):

        print('Enter value for matrix B', i+1,j+1, ':')

        val = int(input())

        B[i][j] = val


for i in range(0,r1):
    for j in range(0,c2):
        C[i][j] = 0
        for k in range(0,r2):
            C[i][j] += A[i][k] * B[k][j]


print('Original Matrix A')
for i in range(0,r1):
    for j in range(0,c1):
        print(A[i][j], end = ' ')
    print()

print('Original Matrix B')
for i in range(0,r2):
    for j in range(0,c2):
        print(B[i][j], end = ' ')
    print()

print('Matrix C after multiplication')
for i in range(0,r1):
    for j in range(0,c2):
        print(C[i][j], end = ' ')
    print()