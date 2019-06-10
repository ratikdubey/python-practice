def fibonnaci(n, a = 0, b = 1):

    if n == 0:
        return

    else:
        print(a)

        a, b = b, (a+b)

        fibonnaci(n-1, a, b)
    return

num = int(input('How many Fibonacci numbers: '))

fibonnaci(num)
