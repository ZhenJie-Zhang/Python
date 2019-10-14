class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

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


def main():
    acc = Account('123456789', 'Tom')
    # acc = Account('','')
    # acc.number = '12324214'
    # acc.name = 'Tommy'
    print(acc.number)
    print(acc.name)

    amount = int(input('輸入存款金額：'))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額：'))
    acc.withdraw(amount)
    print(acc.balance)


main()