r = int(input('Enter number of rows: '))
c = int(input('Enter number of columns: '))

A = [[0 for row in range(r)]for column in range(c)]

print('Original Matrix:', A)

# Matrix A

for i in range(0,r):
    for j in range(0,c):

        print('Enter value for', i+1,j+1, ':')

        val = int(input())

        A[i][j] = val

print('Updated Matrix')
for i in range(0,r):
    for j in range(0,c):
        print(A[i][j], end = ' ')
    '\n'


print('Diagonal Values')
for i in range(0,r):
    for j in range(0,c):
        if i == j or i+j == r - 1:
            print(A[i][j], end = '')
        else:
            print(' ', end = '')
    '\n'


