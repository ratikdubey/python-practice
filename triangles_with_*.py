n = 1
m = 10

for i in range(0, 10, 1):
    while n < 11 and m > 0:
        for j in range(1, i+2, 1):
            print(' '*n, end = '')
            print(' *'*m)
            n += 1
            m -= 1
