class Stack:
    def __init__(self, lst):
        self.lst = lst

    def push(self, num):
        self.lst.append(num)

    def pop(self):
        if self.lst == []:
            print('List is empty!')
        else:
            print(self.lst.pop())

    def peek(self):
        if self.lst == []:
            print('List is empty!')
        else:
            print(self.lst[-1])

    def traverse(self):
        if self.lst == []:
            print('List is empty!')
        else:
            print(self.lst)


obj = Stack([])

print('OPTIONS:\n1 - PUSH\n2 - POP\n3 - PEEK\n4 - Traverse\n5 - EXIT')

n = 0
while n != 5:

    n = int(input('Enter option: '))

    if n == 1:
        num_push = int(input('Enter number to push: '))
        obj.push(num_push)
    elif n == 2:
        obj.pop()
    elif n == 3:
        obj.peek()
    elif n == 4:
        obj.traverse()
    else:
        print('Enter a valid option!')
