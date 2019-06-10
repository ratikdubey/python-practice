a = int(input('Enter a number: '))

num = a

num_rev = 0

while num > 0:
    rem = num % 10
    num = num // 10
    num_rev = (num_rev*10)+rem

print('Reversed number is: {}'.format(num_rev))

if a == num_rev:
    print('Number is a palindrome!')

