class Account:
    def __init__(self, title = None, bal = 0) -> None:
        self.title = title
        self.balance = bal
        
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title = None, bal = 0, interest_rate = 0) -> None:
        super().__init__(title, bal)
        self.interest_rate = interest_rate
    
    def interestAmount(self):
        return (self.interest_rate * self.balance)/100

AC1 = SavingsAccount("Ashish", 2000, 5)
AC1.title, AC1.balance, AC1.interest_rate

AC1.getBalance()

AC1.deposit(500)
AC1.getBalance()

AC1.withdrawal(500)
AC1.getBalance()

AC1.interestAmount()
