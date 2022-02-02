class FundsException(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Available balance is {self.balance}, withdraw amount is {self.amount}"


class SavingsAccount:
    # static or class attributes
    minbal = 10000

    @staticmethod  # decorator
    def getminbal():
        return SavingsAccount.minbal

    @classmethod
    def create(cls, acno, ahname):
        return cls(acno, ahname)

    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def show(self):
        print(self.acno, self.ahname, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise FundsException(amount, self.balance)

    def getbalance(self):
        return self.balance


a = SavingsAccount.create(100, "Tom")
a.show()

print(SavingsAccount.getminbal())  # call static method

s = SavingsAccount(1, "Scott", 100000)
s.deposit(10000)
s.withdraw(200000)
s.show()
print(s.getbalance())

s2 = SavingsAccount(acno=2, ahname="Andy")
s2.show()
