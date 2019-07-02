#Code for a library

class Member:
    def __init__(self):
        self.mem1 = {111:'3 months', 222:'3 months', 333:'6 months', 444:'6 months', 555:'12 months'}
        self.mem2 = {111:'Ratik', 222:'Archit', 333:'Avni', 444:'Pranshu', 555:'Sahil'}

    def show(self):
        self.id = int(input('Enter membership ID: '))
        print(self.mem1.get(id, 'Not a member!'))
        print(self.mem2.get(id, 'Not a member!'))


class Books():
    books = [[11, 'Harry Potter', 'J.K Rowling', '$8', 10], [22, 'Origin', 'Dan Brown', '$9', 7], [33, 'The Innocent', 'David Baldacci', '$7', 6], [44, 'A Prisoner of Birth', 'Jeffery Archer', '$10', 3], ['Think and Grow Rich', 'Napoleon Hill', '$7', 4]]


class Transactions(Member, Books):

    def issue(self):
        flag = 0
        book_id = int(input('Enter ID of book you want to issue: '))
        for item in Books.books:
            if item[0] == book_id:
                print(item[1], 'by', item[2], 'ISSUED!')
                item[4] -= 1
                flag = 1

                lst2 = [item[1], self.id, self.mem2[self.id]]

        if flag == 0:
            print('Book cannot be issued!')



    def returns(self):
        flag = 0

        book_id = int(input('Enter ID of book you want to return: '))
        for item in Books.books:
            if item[0] == book_id:
                print(item[1], 'by', item[2], 'RETURNED!')
                item[4] += 1

                flag  = 1

        if flag == 0:
            print('Book cannot be returned!')




obj = Transactions()
obj.show()


print('OPTIONS\n1 - Issue a book\n2 - Return a book\n3 - EXIT')
option = int(input('Enter option: '))

if option == 1 :
    obj.issue()
elif option == 2 :
    obj.returns()
else :
    print('Enter a valid option!')