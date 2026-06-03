class BankAccount:

    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"{self.owner} Balance: ₹{self._balance}"


if __name__ == "__main__":
    account = BankAccount("Srikanth", 5000)

    account.deposit(1000)
    account.withdraw(500)

    print(account)

