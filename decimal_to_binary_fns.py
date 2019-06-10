from array import *

def dec_bin(num):

    arr = array('i', [])

    while num > 0:
        rem = num % 2
        num = num // 2

        arr.append(rem)

    arr.reverse()

    for i in arr :
        print(i, end='')


dec_bin(int(input('Enter a decimal number: ')))