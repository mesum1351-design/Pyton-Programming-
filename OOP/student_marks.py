
# Create Student class
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Calculate total marks
    def total(self):
        return sum(self.marks)

    # Calculate average marks
    def average(self):
        return self.total() / 3

    # Calculate grade
    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"


# Store five students in a list
students = [
    Student("Ali", 1, [85, 90, 80]),
    Student("Ahmed", 2, [75, 70, 78]),
    Student("Sara", 3, [65, 60, 68]),
    Student("Hamid", 4, [55, 58, 52]),
    Student("Ayesha", 5, [40, 45, 42])
]

# Display all student records
print("Name\tRoll\tTotal\tAverage\tGrade")

for s in students:
    print(s.name, "\t", s.roll, "\t",
          s.total(), "\t",
          round(s.average(), 2), "\t",
          s.grade())
