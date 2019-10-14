class Account:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                    raise ValueError
            self.balance += amount
        except ValueError:
            print('金額必須為正整數')


    def withdraw(self, amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('餘額不足')

    def __str__(self):
        return ('number: {}, name: {}, balance: {}'.format(self.number, self.name, self.balance))


def main():
    acc = Account('123456789', 'Tom', 10000)
    # acc = Account('','')
    # acc.number = '12324214'
    # acc.name = 'Tommy'
    print(acc)
    acc.withdraw(10000)
    print(acc)
    acc.deposit(100)
    acc.name = 'Tommy'
    print(acc)

main()