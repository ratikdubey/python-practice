from collections import *

class Dequeue:
    def __init__(self, lst):
        self.lst = lst

    def add_front(self, num):
        self.lst.appendleft(num)

    def add_rear(self, num):
        self.lst.append(num)

    def delete_front(self) :
        if self.lst == [] :
            print('Queue is empty!')
        else:
            print(self.lst.popleft())

    def delete_rear(self):
        if self.lst == []:
            print('Queue is empty!')
        else:
            print(self.lst.pop())

    def search(self, num_s):
        try:
            print('Element found at position: {}'.format(self.lst.index(num_s)))
        except ValueError:
            print('Element not present in Queue!')


    def display(self):
        if self.lst == []:
            print('Queue is empty!')
        else:
            print(self.lst)

d = deque()
obj = Dequeue(d)

print('OPTIONS:\n1 - ADD FRONT\n2 - ADD REAR\n3 - DELETE FRONT\n4 - DELETE REAR\n5 - SEARCH\n6 - DISPLAY\n7 - EXIT')

n = 0
while n != 7:

    n = int(input('Enter option: '))

    if n == 1:
        num_push = int(input('Enter number to add: '))
        obj.add_front(num_push)
    elif n == 2:
        num_push = int(input('Enter number to add: '))
        obj.add_rear(num_push)
    elif n == 3:
        obj.delete_front()
    elif n == 4:
        obj.delete_rear()
    elif n == 5:
        num_search = int(input('Enter element to search: '))
        obj.search(num_search)
    elif n == 6:
        obj.display()
    else:
        print('Enter a valid option!')
