def count_str(str):
    count1 = 0
    count3 = 0
    len(str)
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count1 += 1
        if i == ' ':
            count3 += 1

    count2 = len(str) - count1

    print('Number of consonants is: {}'.format(count2))
    print('Number of vowels is: {}'.format(count1))
    print('Number of spaces is: {}'.format(count3))



string = str(input('Enter string: '))

count_str(string)