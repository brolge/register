# register code made by brolge
users = [
    {"ID": 1, "Name": "Second, First", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 2, "Name": "Second, First1", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 3, "Name": "Second, First2", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 4, "Name": "Second, First3", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 5, "Name": "Second, First4", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 6, "Name": "Second, First5", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 7, "Name": "Second, First6", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 8, "Name": "Second, First7", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 9, "Name": "Second, First8", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 10, "Name": "Second, First9", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 11, "Name": "Second, First10", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 12, "Name": "Second, First11", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 13, "Name": "Second, First12", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 14, "Name": "Second, First13", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 15, "Name": "Second, First14", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 16, "Name": "Negoescu, Fabian", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 17, "Name": "Second, First15", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 18, "Name": "Second, First16", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 19, "Name": "Second, First17", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 20, "Name": "Second, First18", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 21, "Name": "Second, First19", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 22, "Name": "Second, First20", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 23, "Name": "Second, First21", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 24, "Name": "Second, First22", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 25, "Name": "Second, First23", "Attendance": "", "AccountType": "Student", "Logs": ""},
    {"ID": 26, "Name": "Second, First24", "Attendance": "", "AccountType": "Student", "Logs": ""}
]

# Existing accounts and roles, currently students arent able to sign in by username or password
admin_account = {"username": "admin", "password": "admin", "role": "Admin"}
teacher_account = {"username": "teacher", "password": "teacher", "role": "Teacher"}
student_account = {"username": , "password": "student", "role": "Student"}

# placeholder for now
classrooms = {
    "default": {"students": [1, 2, 3], "teacher": "teacher", "attendance": {}}
}

next_user_id = len(users) + 1  #new userid assigner

# Login function
def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == admin_account["username"] and password == admin_account["password"]:
        admin_access()
    elif username == teacher_account["username"] and password == teacher_account["password"]:
        teacher_access()
    elif username == student_account["username"] and password == student_account["password"]:
        student_access(username)
    else:
        print("Invalid login. Please try again.")
        login()

# Admin acess
def admin_access():
    print("\nWelcome, Admin!")
    while True:
        print("\nAdmin Menu:")
        print("1. Add a student to a class")
        print("2. Remove a student from a class")
        print("3. Create a new class")
        print("4. Assign a teacher to a class")
        print("5. Change a user's role")
        print("6. View all users")
        print("7. Create a new user")
        print("8. Log out")

        choice = input("\nSelect an option: ")
        if choice == "1":
            add_student_to_class()
        elif choice == "2":
            remove_student_from_class()
        elif choice == "3":
            create_class()
        elif choice == "4":
            assign_teacher()
        elif choice == "5":
            change_role()
        elif choice == "6":
            view_all_users()
        elif choice == "7":
            create_new_user()
        elif choice == "8":
            print("You are now logged off")
            login()
        else:
            print("Invalid option. Try again.")

def add_student_to_class():
    student_id = int(input("Enter student ID: "))
    class_name = input("Enter class name: ")

    if class_name in classrooms:
        classrooms[class_name]["students"].append(student_id)
        print(f"Student with ID {student_id} has been added to {class_name}.")
    else:
        print("Class not found.")

def remove_student_from_class():
    student_id = int(input("Enter student ID: "))
    class_name = input("Enter class name: ")

    if class_name in classrooms:
        classrooms[class_name]["students"] = [student for student in classrooms[class_name]["students"] if student != student_id]
        print(f"Student with ID {student_id} has been removed from {class_name}.")
    else:
        print("Class not found.")

def create_class():
    class_name = input("Enter new class name: ")
    if class_name not in classrooms:
        classrooms[class_name] = {"students": [], "teacher": None, "attendance": {}}
        print(f"Class {class_name} created.")
    else:
        print("Class already exists.")

def assign_teacher():
    class_name = input("Enter class name: ")
    teacher_name = input("Enter teacher username: ")
    if class_name in classrooms:
        classrooms[class_name]["teacher"] = teacher_name
        print(f"Teacher {teacher_name} assigned to {class_name}.")
    else:
        print("Class not found.")

def view_all_users():
    print("\nList of all users and their roles:")
    for user in users:
        print(f"ID: {user['ID']}, Name: {user['Name']}, Role: {user['AccountType']}")

# create new user
def create_new_user():
    global next_user_id
    new_name = input("Enter the name of the new user: ")
    new_role = input("Enter the role (Admin/Teacher/Student): ")
    new_user = {"ID": next_user_id, "Name": new_name, "Attendance": "", "AccountType": new_role, "Logs": ""}
    users.append(new_user)
    print(f"New user {new_name} with ID {next_user_id} and role {new_role} created.")
    next_user_id += 1

# New function to change user roles
def change_role():
    user_id = int(input("Enter the ID of the user to change their role: "))
    new_role = input("Enter the new role (Admin/Teacher/Student): ")

    for user in users:
        if user["ID"] == user_id:
            user["AccountType"] = new_role
            print(f"{user['Name']}'s role has been updated to {new_role}.")
            break
    else:
        print("User not found.")

#teacher usage
def teacher_access():
    print("\nWelcome, Teacher!")
    while True:
        print("\nTeacher Menu:")
        print("1. Take attendance")
        print("2. Log out")

        choice = input("\nSelect an option: ")
        if choice == "1":
            take_attendance()
        elif choice == "2":
            break
        else:
            print("Invalid option. Try again.")

def take_attendance():
    class_name = input("Enter class name: ")

    if class_name in classrooms:
        print("\nClass Roster:")
        for student_id in classrooms[class_name]["students"]:
            for user in users:
                if user["ID"] == student_id:
                    print(f"{student_id}: {user['Name']}")

        attendance = input("\nEnter attendance (comma separated student IDs): ")
        attendance_ids = list(map(int, attendance.split(",")))

        for student_id in classrooms[class_name]["students"]:
            if student_id in attendance_ids:
                classrooms[class_name]["attendance"][student_id] = "/"
            else:
                classrooms[class_name]["attendance"][student_id] = "N"

        print("Attendance has been taken.")
    else:
        print("Class not found.")

#student usage
def student_access(username):
    print("\nWelcome, Student!")
    while True:
        print("\nStudent Menu:")
        print("1. View classes and teachers")
        print("2. Log out")

        choice = input("\nSelect an option: ")
        if choice == "1":
            view_classes(username)
        elif choice == "2":
            break
        else:
            print("Invalid option. Try again.")

def view_classes(username):
    student_id = None
    for user in users:
        if user['Name'] == username:
            student_id = user['ID']
            break

    print("\nYour Classes:")
    for class_name, details in classrooms.items():
        if student_id in details["students"]:
            print(f"Class: {class_name}, Teacher: {details['teacher']}")

login()
