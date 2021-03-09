class Account:
    numCreated = 0
    def __init__(self, initial_balance):
        self._balance = initial_balance
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
            print("You are overdrawn and have been charged £20")
            break


    def getbalance(self):
        return self._balance

class Saver(Account):
    numCreated = 0
    def __init__(self, initial_balance):
      super().__init__(initial_balance)  # could use Account
      self._balance = initial_balance
      Saver.numCreated +=1

    def calculate_monthly_interest(self):
        self._interest = (4.5 * self._balance/100)/12
        print("You have earned: £", self._interest, "interest this month")
        self._balance += self._interest
        print("Your current balance is ", self._balance)

class Annualsaver(Saver):
    numCreated = 0
    def __init__(self, initial_balance):
        super().__init__(initial_balance)
        self._balance = initial_balance
        Annualsaver.numCreated += 1



