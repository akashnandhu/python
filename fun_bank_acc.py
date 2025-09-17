class bank_account :
    __bank_balance=28000
    def __init__(self):
        self.bank_balance=28000
        print("welcome")
    def _acc_no(self):
        print("account number is AC-233344564")
    def acc_holder(self):
        print("Akash")
class withrawel(bank_account):
    def withraw(self,amount):
        if(amount<=self.bank_balance):
            self.bank_balance=self.bank_balance-amount
            print("widrawal successful.....!Remaning balance is ",self.bank_balance)
        else:
            print("insufficient balance")
class deposit(withrawel):
    def depo(self,amount):
            self.bank_balance=self.bank_balance+amount
            print("Deposit successful.....!current balance is ",self.bank_balance)
x=withrawel()
x.withraw(3000)
y=deposit()
y.depo(3000) 