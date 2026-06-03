class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}"

    def __repr__(self):
        return f"BankAccount('{self.account_holder}', {self.balance})"


account = BankAccount("Aryan", 100000)
print(account)
account.deposit(10000)
print("After deposit:", account.get_balance())
account.withdraw(10300)
print("After withdrawal:", account.get_balance())
print(repr(account))

account2 = BankAccount("sara", 200000)
print(account2)
account2.deposit(15000)
print("After deposit:", account2.get_balance())
account2.withdraw(30000)
print("After withdrawal:", account2.get_balance())
print(repr(account2))

account3 = BankAccount("Karan", 150000)
print(account3)
account3.deposit(20000)
print("After deposit:", account3.get_balance())
account3.withdraw(20000)
print("After withdrawal:", account3.get_balance())
print(repr(account3))       
