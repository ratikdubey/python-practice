def fibonnaci(n):

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b
        print(a)


fibonnaci(5)