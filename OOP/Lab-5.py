from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def display_details(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_details(self):
        print("Employee Type: Full Time")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

    def display_details(self):
        print("Employee Type: Part Time")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

class ContractEmployee(Employee):
    def __init__(self, name, contract_amount):
        self.name = name
        self.contract_amount = contract_amount
    def calculate_salary(self):
        return self.contract_amount
    def display_details(self):
        print("Employee Type: Contract")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

# Creating objects
e1 = FullTimeEmployee("Ali", 80000)
e2 = PartTimeEmployee("Ahmed", 80, 500)
e3 = ContractEmployee("Sara", 100000)

# Displaying details
e1.display_details()
print()
e2.display_details()
print()
e3.display_details()
