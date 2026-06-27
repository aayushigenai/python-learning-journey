#create account class with two attributes -balance and account .no 
# create methods  for debit , credit  and printing the balance.

class Account:

    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
            self.bal -= amount
            print("Rs.",amount,"was debited.")
            print("account balance :",self.get_balance())

    def credit(self,amount):
            self.bal+=amount
            print("Rs.", amount,"is your balance.")
            print("account balance :",self.get_balance())


    def get_balance(self):
            return self.bal       


a1 = Account(75000,1245)
a1.debit(1000)
a1.credit(500)
    

    