from math import *

# Finding roots for quadratic equation in the form of a(x**2) + b(x) + c

def find_roots(a, b, c):
    d = (b**2 - 4*a*c)

    if d == 0:
        print('Equal roots:')

        root = (-b)/2

        return root

    elif d < 0:
        print('Complex roots:')

        x = (-1*b)/(2*a)
        y1 = sqrt(-1*d)/(2*a)
        y2 = (-1)*sqrt(-1*d)/(2*a)

        root1 = complex(x, y1)
        root2 = complex(x, y2)

        return root1, root2

    else:
        print('Real roots:')

        root1 = (-1*b - sqrt(d))/(2*a)
        root2 = (-1*b + sqrt(d))/(2*a)

        return root1, root2


A = int(input('Enter coefficient for x**2: '))
B = int(input('Enter coefficient for x: '))
C = int(input('Enter coefficient for constant: '))

print(find_roots(A, B, C))