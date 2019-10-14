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


def main():
    acc = Account('123456789', 'Tom', 10000)
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

    acc1 = Account('14564569', 'Marry')
    print(acc1.number)
    print(acc1.name)

    amount = int(input('輸入存款金額：'))
    acc1.deposit(amount)
    print(acc1.balance)
    amount = int(input('輸入提款金額：'))
    acc1.withdraw(amount)
    print(acc1.balance)

main()