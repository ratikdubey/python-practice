from threading import *
from time import *

class Railway:

    def __init__(self, n):
        self.n = n
        self.l = Lock()

    def booking(self, m):
        self.m = m

        self.l.acquire()

        name = current_thread().getName()

        if self.m > self.n or self.n == 0:
            print('{}, number of tickets not sufficient!'.format(name))
        else:
            print('Your tickets have been booked {}!'.format(name))
            self.n -= self.m

        print('Available tickets: {}'.format(self.n))
        self.l.release()



a = int(input('Enter number of available tickets: '))

obj1 = Railway(a)

b = int(input('Enter number of tickets to be booked: '))

t1 = Thread(target = obj1.booking, args = (b,))
t2 = Thread(target= obj1.booking, args=(b,))

t1.setName('Ratik')
t2.setName('Pranshu')

t1.start()
t2.start()
