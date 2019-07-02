from file_emp_class import *
from pickle import *

f = open('file_emp_class.txt2', 'wb')

n = int(input('How many employees: '))

for i in range(n):

    name = input('Enter employee name: ')
    id = int(input('Enter employee id: '))
    salary = int(input('Enter employee salary: '))

    e = Emp(name, id, salary)

    dump(e, f)

f.close()

f = open('file_emp_class.txt2', 'rb')

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

