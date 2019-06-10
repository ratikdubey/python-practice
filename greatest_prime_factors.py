num = int(input('Enter a number: '))

print('Prime factors of {} are:'.format(num))

for i in range(1, num+1):
    k = 0
    if num % i == 0:
        for j in range(2, i):
            if i % j == 0:
                k = 1
                break
        if k == 0:
            print(i)
