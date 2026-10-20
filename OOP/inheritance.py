#1. Single Inheritance
#One child class inherits from one parent class.
# Parent Class
class Vehicle:
  def vehicle_info(self):
    print("Inside Vehicle class")
# Child Class (inherits from Vehicle)
class Car(Vehicle):
  def car_info(self):
    print("Inside Car class")
# Create an object of the child class
car = Car()
# Accessing parent class method using the child object
car.vehicle_info()  # Output: Inside Vehicle class
# Accessing child class method
car.car_info()  # Output: Inside Car class

#2. Multiple Inheritance
#One child class inherits from multiple parent classes

# Parent 1
class Person:
  def person_info(self, name):
    print("Name:", name)
# Parent 2
class Company:
  def company_info(self, company_name):
    print("Company:", company_name)
# Child class inheriting from both
class Employee(Person, Company):
  def employee_role(self):
    print("Role: Developer")
# Object creation
emp = Employee()
emp.person_info("Ali")  # Output: Name: Ali
emp.company_info("Google")  # Output: Company: Google
emp.employee_role()  # Output: Role: Developer


#3. Multilevel Inheritance
# A class inherits from a child class, forming a chain (A - B - C).

# Base class
class Vehicle:
  def vehicle_type(self):
    print("Type: Land Vehicle")
# Child class 1
class Car(Vehicle):
  def car_name(self):
    print("Car: Sedan")
# Child class 2 (inherits from Car)
class SportsCar(Car):

  def boost(self):
    print("Turbo boost activated!")
# Object creation
s_car = SportsCar()
s_car.vehicle_type()  # Output: Type: Land Vehicle
s_car.car_name()  # Output: Car: Sedan
s_car.boost()  # Output: Turbo boost activated!

#4. Hierarchical Inheritance
#Multiple child classes inherit from a single parent class.

# Parent class
class Vehicle:
  def info(self):
    print("This is a general vehicle")
# Child class 1
class Car(Vehicle):
  def car_brand(self, name):
    print("Car brand:", name)
# Child class 2
class Truck(Vehicle):
  def truck_brand(self, name):
    print("Truck brand:", name)
# Object creation
c = Car()
c.info()  # Output: This is a general vehicle
c.car_brand("BMW")  # Output: Car brand: BMW

t = Truck()
t.info()  # Output: This is a general vehicle
t.truck_brand("Ford")  # Output: Truck brand: Ford