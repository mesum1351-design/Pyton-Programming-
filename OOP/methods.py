class Student:
  school_name = "ABC School"  # Class Variable
  def __init__(self, name):
   self.name = name  # Instance Variable
# Instance Method (accesses instance & class variables)
  def show(self):
    print(f"Name: {self.name}, School: {Student.school_name}")
#  Class Method (modifies class variable)
  @classmethod
  def update_school(cls, new_name):
    cls.school_name = new_name
# Usage
s1 = Student("Ali")
s1.show()           # Output: Name: Ali, School: ABC School
# Call class method using the class name
Student.update_school("XYZ School")
s1.show()           # Output: Name: Ali, School: XYZ School