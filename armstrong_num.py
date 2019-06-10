num = int(input('Enter a number: '))

a = num

sum = 0

while num > 0:
    rem = num % 10
    num = num // 10
    cube = rem**3
    sum += cube

print('Sum of cubes of digits is: {}'.format(sum))

if sum == a:
    print('Number is an armstrong number!')
else:
    print('Not an armstrong number!')