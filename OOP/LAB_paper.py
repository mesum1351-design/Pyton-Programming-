#Question 1
myDict = {
"language": "Python",
"type": "interpreted",
"paradigm": "object-oriented",
"ID" : 123,
"purpose": "programming",
"category": "language",
"connector": 2,
"feature": "dynamic",
"concept": "semantics"
}

#i. Add a new key-value pair "binding": "programming" to the dictionary.
myDict.append("binding")
print(myDict)

#ii. Remove the key "concept" and its value from the dictionary.

myDict.remove("concept")
print("After Removing concept and its value")
print(myDict)

#iii. Check whether the key "connector" exists and display its value.
for i in myDict:
    if "conector":
        print("conector: 2")

    print("Not exist")




#Question # 2 (2 Marks)

addresses ={"Ahmad": 'Hafizabad 678', 'Ali': 'Colony 345',
'Rana': 'Rwp 564'}


#i) Return a copy of the Dictionary
print(addresses)
new_addresses = addresses.copy()
print("The copy of addresses")
print(new_addresses)


#ii) Return the keys using loop
for i in addresses:
    print(i)

#iii) Return the items in the dictionary using loop

for i in addresses:
    print(addresses)
    break


#Question 3

# Create a class named bank
class bank:

    # Parameterized constructor
    def __init__(self, accNo, balance, name, type):
        self.accNo = accNo
        self.balance = balance
        self.name = name
        self.type = type

    # Function to display account number
    def display_accNo(self):
        print("Account Number:", self.accNo)

    # Function to display account balance
    def display_balance(self):
        print("Account Balance:", self.balance)

    # Function to display account holder name
    def display_name(self):
        print("Account Holder Name:", self.name)

    # Function to display account type
    def display_type(self):
        print("Account Type:", self.type)


# Get account details from the user
name = input("Enter account holder name: ")
accNo = int(input("Enter account number: "))
balance = float(input("Enter account balance: "))
type = input("Enter account type (Saving/Current): ")

# Create an object of the bank class
account1 = bank(accNo, balance, name, type)

# Call member functions to display account details
print("\n--- Bank Account Details ---")
account1.display_accNo()
account1.display_balance()
account1.display_name()
account1.display_type()


#Question 4
import pandas as pd

# Create a dictionary containing student data
data = {
    'Student Name': [
        'Leonard', 'Penny', 'Howard', 'Bernadette',
        'Sheldon', 'Raj', 'Amy'
    ],
    'Class': ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
    'Section': ['B', 'C', 'A', 'D', 'A', 'B', 'B'],
    'Percentage': [91.2, 63.5, 90.23, 92.7, 98.2, 88.1, 95.0]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete table
print("Complete Student Table:")
print(df.to_string(index=False))

# i) Print only the students belonging to Section A
print("\nStudents belonging to Section A:")
section_A = df[df['Section'] == 'A']
print(section_A.to_string(index=False))

# ii) Calculate section-wise mean percentage
print("\nSection-wise Mean Percentage:")
mean_percentage = df.groupby('Section')['Percentage'].mean()
print(mean_percentage)
