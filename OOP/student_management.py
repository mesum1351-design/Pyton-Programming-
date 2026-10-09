class Course:
    def __init__(self, course_name, course_code, teacher_name):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher_name = teacher_name
        self.students = []

    def add_student(self, name):
        self.students.append(name)
        print(name, "added successfully.")

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
            print(name, "removed successfully.")
        else:
            print(name, "not found.")

    def search_student(self, name):
        if name in self.students:
            print(name, "is enrolled in the course.")
        else:
            print(name, "is not enrolled.")

    def display_students(self):
        print("Course:", self.course_name)
        print("Course Code:", self.course_code)
        print("Teacher:", self.teacher_name)
        print("Students:", self.students)
        print("-------------------")
# Creating 2 course objects
course1 = Course("Python Programming", "CS101", "Mr. Ali")
course2 = Course("Data Science", "CS102", "Ms. Sara")
# Adding students
course1.add_student("Ahmed")
course1.add_student("Mesum")
course1.add_student("Hassan")

course2.add_student("Ali")
course2.add_student("Usman")

# Testing operations
course1.search_student("Mesum")
course1.remove_student("Hassan")
course1.display_students()

course2.search_student("Ali")
course2.display_students()