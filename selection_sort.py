from array import *

arr = array('i', [])

for i in range(0,5):

    num = int(input('Enter element: '))
    arr.append(num)

print('Original array: {}'.format(arr))

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            x = arr[j]
            arr[j] = arr[i]
            arr[i] = x

print('Sorted array: {}'.format(arr))