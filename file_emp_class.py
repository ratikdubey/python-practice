class Emp:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print('Name: {}\nID: {}\nSalary: ${}'.format(self.name, self.id, self.salary))

        