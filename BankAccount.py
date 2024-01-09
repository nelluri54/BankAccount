class CreateBankAccount:
    def __init__(self,name,number,Balance=0):
        self.AccHolderName=name
        self.AccNumber=number
        self.Balance=Balance
    def deposit(self):
        amount=float(input("enter amount to deposit:"))
        self.Balance+=amount
        print("amount successfully deposited.")
    def withdraw(self):
        amount=float(input("enter amount to withdraw:"))
        if amount>self.Balance:
            print("Insufficent amount in your account")
        else:
            self.Balance-=amount
            print("withdraw successfull")
    def display(self):
        print("Current Balance in your Acccount",self.Balance)
def main():
    name=input("enter Account Holder Name:")
    number=int(input("enter Account Number:"))
    print("account created successfully")
    BankAcc=CreateBankAccount(name,number)
    while True:
        print("\nmenu:")
        print("1.Deposit\n2.Withdraw\n3.Display\n4.exit")
        choice=int(input("\nenter your choice:"))
        if choice==1:
            BankAcc.deposit()
        elif choice==2:
            BankAcc.withdraw()
        elif choice==3:
            BankAcc.display()
        else:
             break
        
        
if __name__=="__main__":
    main()