import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("WELCOME TO WORLD OF BANKING!!!!!")

time.sleep(3)
clear_screen()

class Account:
    def __init__(self, acc_number, acc_holder_name, balance=0):
        self.acc_number = acc_number
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount}. Current balance: INR {self.balance}")
        time.sleep(3)
        clear_screen()
        

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn INR {amount}. Current balance: INR {self.balance}")
        else:
            print("Insufficient funds")
        time.sleep(3)
        clear_screen()

    def display_balance(self):
        print(f"Account Number: {self.acc_number}")
        print(f"Account Holder Name: {self.acc_holder_name}")
        print(f"Current Balance: INR {self.balance}")
        time.sleep(3)
        clear_screen()

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self):
        acc_number = int(input("Enter Account Number: "))
        if acc_number in self.accounts:
            print("Account number already exists")
            return
        acc_holder_name = input("Enter Account Holder Name: ")
        initial_balance = float(input("Enter Initial Balance: INR "))
        self.accounts[acc_number] = Account(acc_number, acc_holder_name, initial_balance)
        print("Account created successfully!")

        time.sleep(3)
        clear_screen()

    def get_account(self, acc_number):
        if acc_number in self.accounts:
            return self.accounts[acc_number]
        else:
            print("Account not found")

        time.sleep(3)
        clear_screen()


    def remove_account(self):
        acc_number = int(input("Enter Account Number to remove: "))
        if acc_number in self.accounts:
            del self.accounts[acc_number]
            print("Account removed successfully!")
        else:
            print("Account not found")

        time.sleep(3)
        clear_screen()

bank_name = input("Enter Bank Name: ")
bank = Bank(bank_name)

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Remove Account")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        bank.create_account()
    elif choice == '2':
        acc_number = int(input("Enter Account Number: "))
        account = bank.get_account(acc_number)
        if account:
            amount = float(input("Enter amount to deposit: INR "))
            account.deposit(amount)
    elif choice == '3':
        acc_number = int(input("Enter Account Number: "))
        account = bank.get_account(acc_number)
        if account:
            amount = float(input("Enter amount to withdraw: INR "))
            account.withdraw(amount)
    elif choice == '4':
        acc_number = int(input("Enter Account Number: "))
        account = bank.get_account(acc_number)
        if account:
            account.display_balance()
    elif choice == '5':
        bank.remove_account()
    elif choice == '6':
        print("Thank you for using our bank management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

time.sleep(3)
clear_screen()

print("Press Enter to continue...")
input()