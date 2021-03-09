from class_account import Account, Saver, Annualsaver

jo_account = Account(1000, "Jo", "2 March")
bo_account = Account(200, "Bo", "12 November")

print("_"*25)
print("Current Account details")
print("_"*25)
print("Jo's opening balance: £", jo_account.getbalance())
print("Bo's opening balance: £", bo_account.getbalance())

jo_account.deposit(10987)
jo_account.makecharges()
bo_account.withdraw(500)
bo_account.makecharges()

# check getbalance updates
print("Jo's current balance: £", jo_account.getbalance())
print("Bo's current balance: £", bo_account.getbalance())
print("_"*25)
print()

print("_"*25)
print("Savings Account details")
print("_"*25)

jo_saver = Saver(200, "Jo Kicks", "2 July")
bo_saver = Saver(100000, "Bo Jo", "12 November")
jo_saver.deposit(300)
bo_saver.deposit(100000)

# print(Saver.numCreated)
# print(jo_saver.__class__.__name__) can be used to check correct class has been created

# nb this needs formatting
print("Jo's savings balance before interest is: £", jo_saver.getbalance(),)# uses getbalance() from Account class
print("Jo's updated balance is £", jo_saver.add_monthly_interest()) # uses add_monthly_interest() from Saver class
print("Bo's savings balance before interest is: £", bo_saver.getbalance())
print("Bo's updated balance is £", bo_saver.add_monthly_interest())

print("_"*25)
print("Annual saver details")
print("_"*25)

jo_annualsaver = Annualsaver(1000, "Jo", "9 March")
jo_annualsaver = Annualsaver(1000, "Jo", "2 March")
jo_annualsaver.withdraw(300)
print(jo_annualsaver.__class__.__name__)
print(jo_annualsaver.getbalance())
print(jo_annualsaver.add_monthly_interest())# overrides add_monthly_interest() from Saver class
print("Jo annual interest is £", jo_annualsaver.add_annual_interest())


