# Define the class (Blueprint)
class Person:
  # Constructor to initialize instance variables
  def __init__(self, name, sex, profession):
    self.name = name
    self.sex = sex
    self.profession = profession

  # Instance method (Behavior)
  def show(self):
    print(
        "Name:", self.name, "Sex:", self.sex, "Profession:", self.profession)

# Create an object (Instantiation)
person_1 = Person("Mesum", "Male", "Software Engineer")
# Call the method using the object
person_1.show()