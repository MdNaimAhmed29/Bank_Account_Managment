class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAccountBalance, acctName):
        self.balance = initialAccountBalance
        self.name = acctName
        print(f'Account holder name:{self.name} created .\nBalance={self.balance:.2f}')

    def get_Balance(self):
        print(f"Account holder name:{self.name} created .\nBalance={self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print('\nDeposit Completed Successfully!')
        self.get_Balance()

    def Transactionable(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry,account {self.name} has balance of{self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.Transactionable(amount)
            self.balance -= amount
            print(f'\n withdraw comepleted')
            self.get_Balance()
        except BalanceException as error:
            print(f'withdraw interrupted.{error}')

    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nBegining Transfer")
            self.Transactionable(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'Transfer complete')
        except BalanceException as error:
            print(f'\nTransfer interupted{error}')


class Interest(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.5)
        print(f'\nDeposit Complete')
        self.get_Balance()


class SavingAccount(Interest):
    def __init__(self, initialAccountBalance, acctName):
        super().__init__(initialAccountBalance, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.Transactionable(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f'\nWithdraw complete')
            self.get_Balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted.{error}')




