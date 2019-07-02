from file_emp_class import *
from pickle import *

f = open('file_emp_class.txt', 'rb')

print('Employee Details:', end = '\n\n')

while True:

    try:
        obj = load(f)
        obj.display()
        print()

    except EOFError:
        print('End of file reached!')
        break

f.close()

