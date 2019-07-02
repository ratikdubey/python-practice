num = 4321
n = 4
a = 0

while a < n:

    rem = num % 10

    num = num // 10

    new_num = rem*(10**(n-1)) + num

    num = new_num

    print(new_num)
    
    a += 1






