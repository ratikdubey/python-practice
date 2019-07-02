with open('file_cities.txt', 'wb') as f :
    reclen = 20

    n = int(input('How many entries: '))

    for i in range(n) :
        city = input('Enter name of city: ')

        spaces = (reclen - len(city)) * ' '

        entry = (city + spaces).encode()

        f.write(entry)

