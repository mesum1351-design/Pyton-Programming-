# Student Grades Database Program
students = {}
# Get number of students
num_students = int(input("Enter number of students: "))
# Get number of subjects
num_subjects = int(input("Enter number of grades per student: "))
# Input student data
for i in range(num_students):

    name = input("\nEnter student name: ")
    grades = []
    for j in range(num_subjects):
        marks = int(input(f"Enter grade for subject {j+1}: "))
        grades.append(marks)
    # Calculate student average
    average = sum(grades) / num_subjects
    # Store data in dictionary
    students[name] = {
        "grades": grades,
        "average": average
    }
# Display student information
print("\n========== STUDENT GRADES DATABASE ==========")
print(f"{'Name':<12}", end="")

for i in range(num_subjects):
    print(f"{'Subject '+str(i+1):<12}", end="")
print(f"{'Average':<10}")
print("-" * (12 + num_subjects * 12 + 10))

for name, data in students.items():
    print(f"{name:<12}", end="")
    for grade in data["grades"]:
        print(f"{grade:<12}", end="")
    print(f"{data['average']:<10.2f}")

# Calculate class average for each subject
print("\n========== CLASS SUBJECT AVERAGES ==========")

for j in range(num_subjects):
    total = 0
    for data in students.values():
        total += data["grades"][j]
    subject_average = total / num_students
    print(f"Subject {j+1} Average: {subject_average:.2f}")
