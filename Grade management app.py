student = { }
def add_student(name, grade):
    student[name] = grade
    print(f"Student {name} added with grade {grade}.")

def update_grade(name, grade):
    if name in student:
        student[name] = grade
        print(f"Grade for {name} updated to {grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in student:
        del student[name]
        print(f"Student {name} removed.")
    else:
        print(f"Student {name} not found.")

def view_students():
    if student:
        print("Students and their grades:")
        for name, grade in student.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")


def main():
    while True:
        print("\nGrade Management App")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Remove Student")
        print("4. View Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == '2':
            name = input("Enter student name: ")
            grade = input("Enter new grade: ")
            update_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ")
            remove_student(name)
        elif choice == '4':
            view_students()
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()