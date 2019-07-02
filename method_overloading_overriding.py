class Basic:
# Method overloading
    def sum(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print('Sum is: {}'.format(a+b+c))
        elif a != None and b != None:
            print('Sum is: {}'.format(a + b))
        else:
            print('Enter more than one argument')



class Baby:
# Method overriding
    def sum(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print('NO')
        elif a != None and b != None:
            print('NO')
        else:
            print('Enter more than one argument')


obj = Baby()
obj.sum(2,3)
obj.sum(2,3,4)
obj.sum(1)