from array import *

arr = array('i', [])

for i in range(0,5):

    num = int(input('Enter element: '))
    arr.append(num)

x = int(input('Enter element to search: '))

count = 0

for j in range(0,len(arr)):
    if arr[j] == x:
        print('Index position of element: {}'.format(j))
        count += 1

print('Number of occurrences: {}'.format(count))