from array import *

arr = array('i', [])

a = int(input('How many elements: '))

for i in range(0,a):

    num = int(input('Enter element: '))
    arr.append(num)

print('Original array: {}'.format(arr))

for i in range(1, len(arr)):

    for j in range(i-1, -1, -1):

        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]


print('Sorted array: {}'.format(arr))
