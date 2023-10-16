import sys

class BankAccount:
    name = ""
    balance = 0
    accnumber = ""
    history = []

    @staticmethod
    def update_balance(dcash):
        BankAccount.balance += dcash

    @staticmethod
    def show_balance():
        print(BankAccount.balance)

    @staticmethod
    def homepage():
        print("\033[H\033[2J")
        print("WELCOME TO ATM INTERFACE")
        print("--------------------------")
        print("Select option:")
        print("1. Register")
        print("2. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            BankAccount.register()
        elif choice == 2:
            sys.exit(0)
        else:
            print("Select a value only from the given options.")
            BankAccount.homepage()

    @staticmethod
    def prompt():
        print("WELCOME " + BankAccount.name + "! TO ATM SYSTEM")
        print("---------------------")
        print("Select option:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Check balance")
        print("5. Transaction History")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Transaction.withdraw()
        elif choice == 2:
            Transaction.deposit()
        elif choice == 3:
            Transaction.transfer()
        elif choice == 4:
            Check.check_balance()
        elif choice == 5:
            History.transaction_history()
        elif choice == 6:
            sys.exit(0)

class Transaction:
    @staticmethod
    def withdraw():
        print("----------------")
        print("Enter amount to withdraw:")
        wcash = int(input())
        if wcash <= BankAccount.balance:
            BankAccount.balance -= wcash
            BankAccount.history.append(str(wcash))
            BankAccount.history.append("Withdraw")
            print(f"Amount Rs{wcash}/- withdrawn successfully")
            print("---------------------------")
        else:
            print("Insufficient balance to withdraw the cash")
            print("---------------------------")
        BankAccount.prompt()

    @staticmethod
    def deposit():
        print("----------------")
        print("Enter amount to deposit:")
        dcash = int(input())
        BankAccount.update_balance(dcash)
        BankAccount.history.append(str(dcash))
        BankAccount.history.append("Deposit")
        print(f"Amount Rs.{dcash}/- deposited successfully!")
        print("---------------------------")
        BankAccount.prompt()

    @staticmethod
    def transfer():
        print("Enter the receiving body:")
        s = input()
        print("Enter the account number of the receiving body:")
        num = input()
        print("Enter the amount to be transferred:")
        tcash = int(input())
        if tcash <= BankAccount.balance:
            BankAccount.balance -= tcash
            BankAccount.history.append(str(tcash))
            BankAccount.history.append("Transferred")
            print(f"Amount Rs.{tcash}/- transferred successfully")
            print("---------------------------")
        else:
            print("Insufficient balance to transfer the cash")
            print("---------------------------")

class Check:
    @staticmethod
    def check_balance():
        print("------------------")
        print("The available balance in the bank account:")
        BankAccount.show_balance()
        print("---------------------------")
        BankAccount.prompt()

class History:
    @staticmethod
    def transaction_history():
        print("---------------------")
        print("Transaction History:")
        k = 0
        if BankAccount.balance > 0:
            for i in range(len(BankAccount.history) // 2):
                for j in range(2):
                    print(BankAccount.history[k], end=" ")
                    k += 1
                print("---------------------")
        else:
            print("Your account is empty")

if __name__ == "__main__":
    BankAccount.homepage()
