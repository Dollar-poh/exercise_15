from class_account import Account, Saver, Annualsaver

lisa_account = Account(1000)

bart_account = Account(20)
lisa_account.deposit(10987)
bart_account.withdraw(3765)

print(bart_account)

lisa_account.deposit(50)
print(lisa_account.getbalance())
print(bart_account.getbalance())


lisa_saver = Saver(200)
lisa_saver.deposit(300)
print(Saver.numCreated)
print(lisa_saver.__class__.__name__)
print(lisa_saver.getbalance())
print(bart_account.makecharges())


lisa_annualsaver = Annualsaver(2000)
print(lisa_annualsaver.__class__.__name__)

