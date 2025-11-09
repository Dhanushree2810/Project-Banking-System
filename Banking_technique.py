class Account:
    def __init__(self,name,Account_no,balance):
        self.name = name
        self.Account_no = Account_no
        self.balance = balance
    def check_balance(self):
        print(f"Account holder name is {self.name}\n Account_no is {self.Account_no}\n Balance is {self.balance}")
    def deposit(self,amount):
        self.balance += amount
        print(f"The ammount deposited is {self.balance}")
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"The amount withdrawn is {self.balance}")
        else:
            print("Insufficient Balance")
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount >= 1000:
            super().withdraw(amount)
        else:
            print("Maintain Minimum Balance")
name = input("Enter the name of the person: ")
Account_no = int(input("Enter the account_no: "))
a = SavingsAccount(name,Account_no,50000)
a.check_balance()
a.deposit(20000)
a.withdraw(69110)
a.check_balance()