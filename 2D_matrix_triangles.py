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

# For bottom left triangle
print('Bottom left triangle')
for i in range(0, r1):
    for j in range(0, c1):
        if j <= i:
            print(A[i][j], end = ' ')
    print()

print()

# For top left triangle
print('Top left triangle')
for i in range(0, r1):
    for j in range(0, c1):
        if (i + j) <= 2:
            print(A[i][j], end = ' ')
        else:
            print(' ', end = ' ')
    print()

print()

# For bottom right triangle
print('Bottom right triangle')
for i in range(0, r1):
    for j in range(0, c1):
        if (i + j) >= 2:
            print(A[i][j], end = ' ')
        else:
            print(' ', end = ' ')
    print()

print()

# For top right triangle
print('Top right triangle')
for i in range(0, r1):
    for j in range(0, c1):
        if  j >= i:
            print(A[i][j], end = ' ')
        else:
            print(' ', end = ' ')
    print()

print()