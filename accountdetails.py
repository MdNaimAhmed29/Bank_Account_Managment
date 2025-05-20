from accountdata import *
Naim=BankAccount(10000, 'Naim')
Akhi=BankAccount(20000,'Akhi')
Naim.deposit(5000)
Naim.withdraw(20000)
Naim.withdraw(10)
Naim.transfer(10000,Akhi)

jim=Interest(1000,'Jim')
jim.get_Balance()
jim.deposit(100)
jim.transfer(100,Naim)


Blaze=SavingAccount(1000,'Blaze')
Blaze.get_Balance()
Blaze.deposit(100)
Blaze.transfer(300,Naim)
