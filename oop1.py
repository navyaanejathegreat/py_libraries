class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        
        self.menu()
        
    def menu(self):
        user_input=input("""
Hello, how would you like to proceed?
Enter 1 to create pin
Enter 2 to deposit money
Enter 3 to withdraw
Enter 4 to check balance
Enter 5 to exit
""")
        if user_input=="1":
            self.Create_pin()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="2":
            self.deposit()
        elif user_input=="4":
            self.check_balance()
        else:
            print ("bye")
            
    def Create_pin(self):
        self.pin=input("Enter your pin:")
        print("Pin set successfully")
    def deposit(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter your amount:"))
            self.balance= self.balance+amount
            print("deposit successful")
        else:
            print("invalid pin")
    def withdraw(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter your amount:"))
            if amount< self.balance:
                self.balance= self.balance-amount
                print("withdrawl successful")
            else:
                print("Insufficient funds")
        else:
            print("invalid pin")
    def check_balance(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        
        
            
            
            
obj2= Atm()