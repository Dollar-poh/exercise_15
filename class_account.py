class Account:
    numCreated = 0

    def __init__(self, initial_balance, name, account_open_date):
        self._balance = initial_balance
        self._name = name
        self._date_of_birth = account_open_date
        Account.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        self._balance -= amount
        return

    # apply overdraft charges if below zero
    def makecharges(self):
        while self._balance < 0:
            self._balance -= 20
            print(self._name, "You are overdrawn and have been charged £20")
            break

    def getbalance(self):
        return self._balance


# create child class of Account and add attribute of interest rate
class Saver(Account):
    numCreated = 0

    def __init__(self, initial_balance, name, account_open_date):
        super().__init__(initial_balance, name, account_open_date)
        self.interest_rate = 0.36
        self._balance = initial_balance
        Saver.numCreated += 1

    def add_monthly_interest(self): # new method in child class
        self._interest = self.interest_rate * self._balance
        print("interest earned: £", self._interest, "interest this month")
        self._balance += self._interest
        return self._balance

# create child class of Saver
class Annualsaver(Saver):
    numCreated = 0

    def __init__(self, initial_balance, name, account_open_date):
        super().__init__(initial_balance, name, account_open_date)
        self._balance = initial_balance
        self._interest_rate = 5.8
        self._account_open_date = account_open_date # would use to calculate time of interest payment
        Annualsaver.numCreated += 1

    # override def from Saver() as only yearly interest to be paid
    def add_monthly_interest(self):
        print("Monthly interest is not applied to this account")

    def add_annual_interest(self):  # new method nb would check opening date before adding annual interest with account_open_date
            self._balance = self.interest_rate * self._balance
            return self._balance

