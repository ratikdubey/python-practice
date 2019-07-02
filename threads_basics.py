from threading import *
from time import *

class Movie:

    tickets = 2

    def __init__(self, n):
        self.n = n

    def get_ticket(self):

        if self.n <= Movie.tickets:
            print('You get {} tickets.'.format(self.n))
            Movie.tickets -= self.n
            print('Tickets left: {}'.format(Movie.tickets))
        else:
            print('Number of tickets available not sufficient!')

    def display(self):
        if Movie.tickets == 0:
            print('No tickets left!')
        else:
            print('Number of tickets left is {}'.format(Movie.tickets))


n1 = int(input('Enter tickets for first object: '))
n2 = int(input('Enter tickets for second object: '))


obj1 = Movie(n1)
obj2 = Movie(n2)

t1 = Thread(target = obj1.get_ticket)
t2 = Thread(target = obj2.get_ticket)


t1.start()
t2.start()