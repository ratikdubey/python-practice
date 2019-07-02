from file_emp_class import *
from pickle import *

f = open('file_emp_class.txt', 'wb')

n = int(input('How many employees: '))

for i in range(n):

    name = input('Enter employee name: ')
    id = int(input('Enter employee id: '))
    salary = int(input('Enter employee salary: '))

    e = Emp(name, id, salary)

    dump(e, f)

f.close()
