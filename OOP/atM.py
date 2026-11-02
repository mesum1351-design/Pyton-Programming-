from abc import ABC, abstractmethod


# ==========================================
# C. Decorator: Transaction se pehle aur baad message dikhana
# ==========================================
def transaction_logger(func):
    def wrapper(self, amount):
        print("\n[★★★ Transaction Shuru ★★★]")
        func(self, amount)
        print("[★★★ Transaction Khatam ★★★]\n")

    return wrapper


# ==========================================
# A & B. Abstract Class aur @property (Balance Security)
# ==========================================
class Account(ABC):
    def __init__(self, acc_number, initial_balance):
        self.number = acc_number
        self._balance = initial_balance  # Private variable
        self.transactions = []  # D. Transactions list mein save hongi

    # Getter: Balance dekhne ke liye
    @property
    def balance(self):
        return self._balance

    # Setter: Balance negative hone se rokne ke liye
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("❌ Error: Balance negative (0 se kam) nahi ho sakta!")
        else:
            self._balance = value

    @transaction_logger
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Yahan setter use ho raha hai
            self.transactions.append(f"Deposit: +{amount}")
            print(f"✅ {amount} jama ho gaye. Naya Balance: Rs.{self.balance}")

    # Abstract Method: Jo child classes ko banana lazmi hai
    @abstractmethod
    def withdraw(self, amount):
        pass


# ==========================================
# A. Child Classes (Saving aur Current Account)
# ==========================================
class SavingAccount(Account):
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"✅ {amount} nikal liye. Baqi Balance: Rs.{self.balance}")
        else:
            print("❌ Error: Account mein itne paise nahi hain!")


class CurrentAccount(Account):
    @transaction_logger
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print(f"✅ {amount} nikal liye. Baqi Balance: Rs.{self.balance}")
        else:
            print("❌ Error: Account mein itne paise nahi hain!")


# ==========================================
# Customer Class
# ==========================================
class Customer:
    def __init__(self, name, pin, account):
        self.name = name
        self.pin = pin
        self.account = account


# ==========================================
# D. Store Customers in a List
# ==========================================
c1 = Customer("Ali", "1234", SavingAccount("SA-101", 5000))
c2 = Customer("Mesum", "5678", CurrentAccount("CA-202", 10000))

customers_list = [c1, c2]

# ==========================================
# E. Loop aur If-Else Menu (ATM System)
# ==========================================
print("=== WELCOME TO PYTHON BANK ===")
entered_pin = input("Apna 4-digit PIN enter karein (Test PIN: 1234 ya 5678): ")

# Customer dhoondna
current_user = None
for cust in customers_list:
    if cust.pin == entered_pin:
        current_user = cust
        break

if current_user:
    print(f"\nWelcome {current_user.name}!")

    while True:
        print("\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Transaction History\n5. Exit")
        choice = input("Kya karna chahte hain? (1-5): ")

        if choice == '1':
            amt = float(input("Kitne paise jama karne hain?: "))
            current_user.account.deposit(amt)

        elif choice == '2':
            amt = float(input("Kitne paise nikalne hain?: "))
            current_user.account.withdraw(amt)

        elif choice == '3':
            print(f"\n💰 Aapka Balance hai: Rs.{current_user.account.balance}")

        elif choice == '4':
            print("\n📜 Transaction History:")
            for record in current_user.account.transactions:
                print(record)

        elif choice == '5':
            print("Bank aane ka shukriya. Allah Hafiz!")
            break
        else:
            print("❌ Galat choice. Dobara koshish karein.")
else:
    print("❌ Galat PIN. System band ho raha hai.")