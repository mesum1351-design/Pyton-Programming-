from abc import ABC, abstractmethod
# C. Decorator: Display messages before and after a transaction
def transaction_logger(func):
    def wrapper(self, amount):
        print("\n[★★★ Transaction Started ★★★]")
        func(self, amount)
        print("[★★★ Transaction Completed ★★★]\n")
    return wrapper
# A & B. Abstract Class and @property (Balance Security)
class Account(ABC):
    def __init__(self, acc_number, initial_balance):
        self.number = acc_number
        self._balance = initial_balance  # Private variable
        self.transactions = []  # Store transactions in a list
    # Getter: To access account balance
    @property
    def balance(self):
        return self._balance
    # Setter: Prevent negative balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: Balance cannot be negative!")
        else:
            self._balance = value
    # Deposit money
    @transaction_logger
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Using the setter
            self.transactions.append(f"Deposit: +{amount}")
            print(f"{amount} deposited successfully. New Balance: Rs.{self.balance}")
    # Abstract Method: Child classes must implement this method
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingAccount(Account):
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"{amount} withdrawn successfully. Remaining Balance: Rs.{self.balance}")
        else:
            print("Error: Insufficient balance in the account!")
class CurrentAccount(Account):
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"{amount} withdrawn successfully. Remaining Balance: Rs.{self.balance}")
        else:
            print("Error: Insufficient balance in the account!")
# Customer Class
class Customer:
    def __init__(self, name, pin, account):
        self.name = name
        self.pin = pin
        self.account = account
# D. Store Customers in a List
c1 = Customer("Ali", "1234", SavingAccount("SA-101", 5000))
c2 = Customer("Mesum", "5678", CurrentAccount("CA-202", 10000))

customers_list = [c1, c2]
# E. Loop and If-Else Menu (ATM System)
print("=== WELCOME TO PYTHON BANK ===")

entered_pin = input("Enter your 4-digit PIN (Test PIN: 1234 or 5678): ")

# Find the customer
current_user = None

for cust in customers_list:
    if cust.pin == entered_pin:
        current_user = cust
        break
if current_user:
    print(f"\nWelcome {current_user.name}!")
    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("What would you like to do? (1-5): ")

        if choice == '1':
            amt = float(input("Enter the deposit amount: "))
            current_user.account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter the withdrawal amount: "))
            current_user.account.withdraw(amt)
        elif choice == '3':
            print(f"\nYour Current Balance is: Rs.{current_user.account.balance}")
        elif choice == '4':
            print("\nTransaction History:")
            for record in current_user.account.transactions:
                print(record)
        elif choice == '5':
            print("Thank you for using our bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. System is shutting down.")
