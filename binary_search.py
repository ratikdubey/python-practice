from array import *

arr = array('i', [])

a = int(input('How many elements: '))

for i in range(0,a):

    num = int(input('Enter element: '))
    arr.append(num)

b = int(input('Enter element to search: '))



low = 0
high = len(arr) - 1

d = 0

while d < len(arr):

    mid = (low+high)//2
    x = arr[mid]

    if x > b:
        low = 0
        high = mid
    else:
        low = mid
        high = len(arr) - 1

    if x == b:
        print('Element found at index position {}'.format(mid))
        break

    d += 1

    if d == len(arr)-1:
        print('Element not found!')

