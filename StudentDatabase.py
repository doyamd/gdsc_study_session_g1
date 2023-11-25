from collections import defaultdict


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student_dict = defaultdict(lambda: Student("", 0, 0))
ID = 0
def add():
    global ID
    ID += 1
    student = Student("", 0, 0)
    print("Please Enter the name of the student: ")
    student.name = input()
    print("Please Enter the age of the student: ")
    student.age = int(input())
    print("Please Enter the grade of the student: ")
    student.grade = int(input())
    student_dict[ID] = student
    print("Registration Completed!")
    return
def update():
    global ID
    print("Enter the ID or name of the student: ")
    id = int(input())
    if id not in student_dict.keys():
        print("Student not found :(")
        return
    student = student_dict[id]
    print("Name: " + student.name)
    print("Age: " + str(student.age))
    print("Grade: " + str(student.grade))
    print("Press 1 to change age, Press 2 to change grade: ")
    pressed = input()
    if pressed == "1":
        print("Enter the new Age: ")
        age = int(input())
        student.age = age
    elif pressed == "2":
        print("Enter the new Grade: ")
        grade = int(input())
        student.grade = grade
    else:
        print("Invalid input!")
    return 
    
def view():
    global ID
    print("Enter the name of the student: ")
    id = int(input())
    if id not in student_dict.keys():
        print("Student not found :(")
        return
    student = student_dict[id]
    print("Name: " + student.name)
    print("Age: " + str(student.age))
    print("Grade: " + str(student.grade))
    return
def viewAll():
    global ID
    print("*****LIST OF ALL STUDENTS*****")
    if not student_dict:
        print("Database Empty") 
    for key, value in student_dict.items():
        print(str(key) + "   " + value.name + "   " + str(value.age) + "   " + str(value.grade))
    return
def delete():
    global ID
    print("Enter the ID or name of the student: ")
    id = int(input())
    del student_dict[id]
    print("Deleted Sucessfully!")

def main():
    while True:
        print("********Student Database********")
        print("1. Add a student")
        print("2. Search a student")
        print("3. Update a student data")
        print("4. Delete a student")
        print("5. View entire database")
        print("6. Exit")
        choice = int(input())
        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            viewAll()
        elif choice == 6:
            print("Exiting Program...")
            break
        else:
            print("Incorrect input.")
main()
        

    
    

