class Student:
  def __init__(self, name, age):
    self.name = name  # Public variable
    self.__age = age  # Private variable (hidden)
# Getter method to read private variable
  def get_age(self):
    return self.__age
# Setter method to modify private variable with a rule
  def set_age(self, new_age):
    if new_age > 0:
      self.__age = new_age
    else:
      print("Invalid age!")
# Usage
s1 = Student("Ali", 14)
# Accessing public variable works directly
print(s1.name)  # Output: Ali
# Accessing private variable via Getter
print(s1.get_age())  # Output: 14
# Modifying private variable via Setter
s1.set_age(16)
print(s1.get_age())  # Output: 16