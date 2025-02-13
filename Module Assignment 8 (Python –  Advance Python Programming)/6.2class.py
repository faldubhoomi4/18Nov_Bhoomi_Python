class bank:
    balance = 0
    account_number=0
    account_holder_name=''
    account_type=''
  

    def accountDetail(self ):
        self.account_number = input("Enter account number: ")
        self.account_holder_name = input("Enter account holder name: ")
        self.account_type = input("Enter account type (Savings/Current): ")
        self.balance = 0
        

    def deposite(self):
        amount = float(input("Enter amount to deposit (minimum $2000): "))
        if amount >= 2000:
            print("Please Deposite value..")
        
            self.balance  += amount
        else:
            print("Error... ")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount < self.balance:
        
            self.balance -= amount
            print("Withdrawal successful..")
        else:
            print("Error... ")
    def statement(self):
        print("Accont statment")
        print("A/c Number:", self.account_number)
        print("A/c Holder name:", self.account_holder_name)
        print("Type:", self.account_type)
        print("total balance:", self.balance )

    
bn = bank()
bn.accountDetail()
while True:
    print("\n--- Bank Management System ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Print Account Statement")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        bn.deposite()
    elif choice == '2':
        bn.withdraw()
    elif choice == '3':
        bn.statement()
    elif choice == '4':
        print("Exiting ")
        break
    else:
        print("Invalid choice. Please try again.")