class Linkedlist:

    def __init__(self, lst):
        self.lst = lst

    def insert(self, pos, num):
        self.lst.insert(pos, num)

    def remove(self, num):
        if self.lst == []:
            print('List is empty!')
        else:
            print(self.lst.pop(self.lst.index(num)))

    def search(self, num_s) :
        try:
            print('Element found at position: {}'.format(self.lst.index(num_s)))
        except ValueError:
            print('Element not present in List!')

    def display(self):
        if self.lst == []:
            print('List is empty!')
        else:
            print(self.lst)


obj = Linkedlist([])

print('OPTIONS:\n1 - INSERT\n2 - REMOVE\n3 - SEARCH\n4 - DISPLAY\n5 - EXIT')

n = 0
while n != 5:

    n = int(input('Enter option: '))

    if n == 1:
        num_push = int(input('Enter number to insert: '))
        num_pos = int(input('Enter position for insertion: '))
        obj.insert(num_pos, num_push)
    elif n == 2:
        num_rem = int(input('Enter number for removal: '))
        obj.remove(num_rem)
    elif n == 3:
        num_search = int(input('Enter element to search: '))
        obj.search(num_search)
    elif n == 4:
        obj.display()
    else:
        print('Enter a valid option!')
