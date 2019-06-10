def sum_of_digits(num):

    sum = 0

    if num == 0:
        return 0

    else:
        rem = num % 10
        num = num // 10
        sum = rem + sum_of_digits(num)

    return sum


n = int(input('Enter number: '))

obj = sum_of_digits(n)

print(obj)