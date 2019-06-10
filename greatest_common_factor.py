a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print('Greatest common factor of {} and {} is:'.format(a, b), end = ' ')

gcf = 0

for i in range(1,(min(a,b)+1)):
    if a % i == 0 and b % i == 0 and i > gcf:
            gcf = i
print(gcf)