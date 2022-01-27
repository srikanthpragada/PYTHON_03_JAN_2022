class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def show(self):
        print(self.acno, self.ahname, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def getbalance(self):
        return self.balance


s = SavingsAccount(1, "Scott", 100000)
s.deposit(10000)
s.show()
print(s.getbalance())

s2 = SavingsAccount(acno=2, ahname="Andy")
s2.show()
