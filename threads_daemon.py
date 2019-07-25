from threading import *
from time import *

def display():
    for i in range(5):
        print('Normal Thread: {}'.format(i+1))
        sleep(1)

def display_time():
    while True:
        print('Daemon Thread: {}'.format(ctime()))
        sleep(1.5)

t = Thread(target = display)
t.start()

d = Thread(target = display_time)
d.daemon = True
d.start()

#d.join()