class Bank:

    def __init__(self, bal, acc_num):
        self.bal = bal
        self.min_bal = 10000
        self.acc_num = acc_num


    def withdraw(self):
        w_amt = int(input('Enter amount for withdrawal: '))

        if self.bal >= self.min_bal:
            if (self.bal - w_amt) >= self.min_bal:
                self.bal -= w_amt
                print('Amount withdrawn: {}'.format(w_amt))
                print('Available balace: {}'.format(self.bal))
            else:
                print('Minimum balance not sufficient for withdrawal!')
        else :
            print('Minimum balance not sufficient for withdrawal!')


    def deposit(self):
        d_amt = int(input('Enter amount to be deposited: '))

        self.bal += d_amt
        print('Amount deposited: {}'.format(d_amt))
        print('Available balance; {}'.format(self.bal))


    def check_bal(self):
        print('Available Balance is: {}'.format(self.bal))


    def options(self, obj):

        print('Enter 1 to DEPOSIT\nEnter 2 to WITHDRAW\nEnter 3 to CHECK BALANCE\nEnter 4 to EXIT')

        num = int(input('Enter option: '))

        account = int(input('Enter account number: '))

        if account in acc:


        while num != 4:
            print('Enter 1 to DEPOSIT\nEnter 2 to WITHDRAW\nEnter 3 to CHECK BALANCE\nEnter 4 to EXIT')
            num = int(input('Enter option: '))

            if num == 1:
                obj.deposit()
            elif num == 2:
                obj.withdraw()
            elif num == 3:
                obj.check_bal()
            else:
                print('Enter a valid input')
                break

        print('Thankyou!')


obj = Bank(25000, 111)
obj.options()