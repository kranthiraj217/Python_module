class Account:
    def __init__(self, title, bal) -> None:
        self.title = title
        self.balance = bal

class SavingsAccount(Account):
    def __init__(self, title, bal, interest_rate) -> None:
        super().__init__(title, bal)
        self.interest_rate = interest_rate

AC1 = SavingsAccount("Ashish", 5000, 5)
AC1.title, AC1.balance, AC1.interest_rate
