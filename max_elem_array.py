from array import *

arr = array('i', [])

for i in range(0,5):

    num = int(input('Enter element: '))
    arr.append(num)

    max1 = 0
    max2 = 0

    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i


print('Array is: {}'.format(arr))
print('2nd max element in array is: {}'.format(max2))


