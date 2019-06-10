num = int(input('Enter a number: '))

print('Greatest factor of {} is:'.format(num), end = ' ')

gf = 0

for i in range(1,num):
    if num % i == 0 and i > gf:
        gf = i
print(gf)