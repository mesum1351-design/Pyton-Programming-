from functools import wraps
# Decorator 1: Check login
def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.logged_in:
            print("Access Denied: Please login first.")
            return

        return func(self, *args, **kwargs)
    return wrapper
# Decorator 2: Check admin access
def admin_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.role != "admin":
            print("Access Denied: Admin only.")
            return
        return func(self, *args, **kwargs)

    return wrapper
# Decorator 3: Log activity
def log_activity(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print("Activity:", func.__name__, "was called")
        return func(self, *args, **kwargs)

    return wrapper
# Decorator 4: Validate student name
def validate_input(func):
    @wraps(func)
    def wrapper(self, name, *args, **kwargs):
        if not isinstance(name, str) or not name.strip():
            print("Invalid Input: Name cannot be empty.")
            return
        return func(self, name, *args, **kwargs)
    return wrapper
class StudentManagement:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.logged_in = False
        self.students = []

    def login(self):
        self.logged_in = True
        print(self.username, "logged in successfully.")
    @login_required
    @log_activity
    def view_students(self):
        print("Student List:", self.students)
    @login_required
    @admin_required
    @log_activity
    @validate_input
    def add_student(self, name):
        self.students.append(name)
        print(name, "added successfully.")
    @login_required
    @admin_required
    @log_activity
    def delete_student(self, name):
        if name in self.students:
            self.students.remove(name)
            print(name, "deleted successfully.")
        else:
            print("Student not found.")
# Testing with an admin
admin = StudentManagement("Ali", "admin")

admin.view_students()   # Not logged in
admin.login()

admin.add_student("Ahmed")
admin.add_student("Sara")
admin.view_students()

admin.add_student("")   # Invalid input
admin.delete_student("Ahmed")
admin.view_students()

print("\nTesting with a normal user:")

user = StudentManagement("Usman", "student")
user.login()
user.view_students()
user.add_student("Hassan")  # Admin access denied
