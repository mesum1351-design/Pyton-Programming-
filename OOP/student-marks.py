
# Store student data
students = {}

# Get number of students and subjects
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

# Input student names and marks
for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(m):
        grade = int(input("Enter marks: "))
        marks.append(grade)

    students[name] = marks

# Display student data and average
print("\nName\tMarks\t\tAverage")

for name, marks in students.items():
    avg = sum(marks) / m
    print(name, "\t", marks, "\t", avg)

# Calculate subject averages
print("\nSubject Averages:")

for j in range(m):
    total = 0

    for marks in students.values():
        total = total + marks[j]

    print("Subject", j + 1, "Average:", total / n)
