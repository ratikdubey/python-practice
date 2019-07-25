from threading import *
from time import *

class Railway:

    def __init__(self, available):
        self.available = available
        self.l = Lock()

    def reserve(self, wanted):

        self.l.acquire()

        print('No. of available births: {}'.format(self.available))

        if self.available >= wanted:
            name = current_thread().getName()
            print('{} births alloted to {}'.format(wanted, name))

            sleep(1.5)

            self.available -= wanted

        else:
            print('Sorry, no berths available')

        self.l.release()

obj1 = Railway(1)

t1 = Thread(target = obj1.reserve, args = (1,))
t2 = Thread(target = obj1.reserve, args = (1,))

t1.setName('Ratik')
t2.setName('Archit')

t1.start()
t2.start()
