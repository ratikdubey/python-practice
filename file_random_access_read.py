with open('file_cities.txt', 'rb') as f:

    reclen = 20

    n = int(input('Which entry: '))

    f.seek(reclen*(n-1))

    str = f.read(reclen)

    print(str.decode())

