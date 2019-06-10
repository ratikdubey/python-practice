from array import *

def sliding_window(arr, n):

    i = 0
    j = n
    counter = 1

    windows = len(arr) - n

    for w in range(windows+1):
        max = 0
        for k in range(i, j):
            if arr[k] > max:
                max = arr[k]

        print('Max element in window {} is: {}'.format(counter, max))

        i += 1
        j += 1
        counter += 1


obj = array('i', [])

elem = int(input('Enter number of elements in array: '))

for i in range(elem):
    num = int(input('Enter element of array: '))
    obj.append(num)

win_size = int(input('Enter window size: '))


sliding_window(obj, win_size)
