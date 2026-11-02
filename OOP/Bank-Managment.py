
from abc import ABC, abstractmethod

# Decorator for transactions
def transaction(func):
    def wrapper(*args):
        print("Transaction started")
        func(*args)
        print("Transaction completed")
    return wrapper


# Abstract Account class
class Account(ABC):
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    # Get balance
    @property
    def balance(self):
        return self._balance

    # Set balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

    @abstractmethod
    def show_account(self):
        pass

    # Deposit money
    @transaction
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    # Withdraw money
    @transaction
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")


# Current Account
class CurrentAccount(Account):
    def show_account(self):
        print("Current Account:", self.name, self.balance)


# Saving Account
class SavingAccount(Account):
    def show_account(self):
        print("Saving Account:", self.name, self.balance)


# Store customer accounts in a list
accounts = [
    CurrentAccount("Hamid", 5000),
    SavingAccount("Ahmad", 8000)
]

# Store transaction records
records = []

# Display customer accounts
for account in accounts:
    account.show_account()

# Menu
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "4":
        print("Goodbye!")
        break

    # Select customer
    for i, account in enumerate(accounts):
        print(i + 1, account.name)

    customer = int(input("Select customer number: ")) - 1

    if customer < 0 or customer >= len(accounts):
        print("Invalid customer")
        continue

    account = accounts[customer]

    if choice == "1":
        amount = int(input("Enter amount: "))
        old_balance = account.balance
        account.deposit(amount)
        if amount > 0 and account.balance != old_balance:
            records.append("Deposit: " + account.name)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        old_balance = account.balance
        account.withdraw(amount)
        if amount > 0 and account.balance < old_balance:
            records.append("Withdraw: " + account.name)

    elif choice == "3":
        print("Balance:", account.balance)

    else:
        print("Invalid choice")
# Display transaction records
print("\nTransaction Records:")
for record in records:
    print(record)
