# To create the BankAccount class
class bank:
    def __init__(self):
        self.bal = 0
        print("Welcome to the SBI")

    def deposit(self):
        amt=float(input("Enter amount to be Deposited: "))
        self.bal +=amt

    def withdraw(self):
        amt=float(input("Enter amount to be Withdraw: "))
        if self.bal>=amt:
            self.bal-=amt
            print("\nYou Withdraw:",amt)
        else:
            print("\nInsufficient balance")

    def display(self):
            print("\nNet Available Balance",self.bal)


#driver code
s=bank()

s.deposit()
s.withdraw()
s.display()

