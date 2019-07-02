class Queue:
    def __init__(self, lst):
        self.lst = lst

    def add(self, num):
        self.lst.append(num)

    def delete(self):
        if self.lst == []:
            print('Queue is empty!')
        else:
            print(self.lst.pop(0))

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


obj = Queue([])

print('OPTIONS:\n1 - ADD\n2 - DELETE\n3 - SEARCH\n4 - DISPLAY\n5 - EXIT')

n = 0
while n != 5:

    n = int(input('Enter option: '))

    if n == 1:
        num_push = int(input('Enter number to add: '))
        obj.add(num_push)
    elif n == 2:
        obj.delete()
    elif n == 3:
        num_search = int(input('Enter element to search: '))
        obj.search(num_search)
    elif n == 4:
        obj.display()
    else:
        print('Enter a valid option!')
