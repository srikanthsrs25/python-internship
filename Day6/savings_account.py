from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, owner, balance=0, interest_rate=5):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self._balance * self.interest_rate) / 100
        self._balance += interest

        print(f"Interest Added: ₹{interest}")


if __name__ == "__main__":

    savings = SavingsAccount("Sam", 10000, 10)

    print(savings)

    savings.add_interest()

    print("Updated Balance:", savings.get_balance())
