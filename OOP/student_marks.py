
# Student Record Management System

# Step 1: Create Student class
class Student:
    def __init__(self, name, roll_no, marks1, marks2, marks3):
        self.name = name
        self.roll_no = roll_no
        self.marks = [marks1, marks2, marks3]

    # Step 2: Calculate total marks
    def total_marks(self):
        return sum(self.marks)

    # Step 3: Calculate average marks
    def average_marks(self):
        return self.total_marks() / 3

    # Step 4: Calculate grade
    def calculate_grade(self):
        avg = self.average_marks()

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


# Step 5: Store five student objects in a list
students = [
    Student("Ali", 101, 85, 90, 80),
    Student("Ahmed", 102, 70, 75, 80),
    Student("Sara", 103, 60, 65, 70),
    Student("Ayesha", 104, 50, 55, 60),
    Student("Usman", 105, 30, 40, 45)
]


# Step 6: Display all student records using a loop
print("========== STUDENT RECORDS ==========")

for student in students:
    print("\nStudent Name:", student.name)
    print("Roll Number:", student.roll_no)
    print("Marks:", student.marks)
    print("Total Marks:", student.total_marks())
    print("Average Marks:", student.average_marks())
    print("Grade:", student.calculate_grade())
    print("-------------------------------------")
