num = int(input('Enter a number: '))

print('Prime numbers between 0 and {} are:'.format(num))

for i in range(1, num+1):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k = 1
    if k == 0:
        print(i)