class Account():
    def _init_(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print(f"owner is {owner}")
        print(balance)
    def deposit(self,D):
        self.D=D
        print(f"Deposit succes : {D}")
        self.balance+=D
        print(f"Total Balance : {self.balance}")
    def withdraw(self,W):
        self.W=W
        if W<=self.balance:
            print("Accepted")
        else:
            print("Low Balance")    
                
a=Account() 
a._init_('phani',1000)   
a.deposit(1000)
a.withdraw(2500)
