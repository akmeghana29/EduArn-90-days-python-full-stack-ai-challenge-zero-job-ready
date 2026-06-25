# Student Marks Management System

# storing student data in a dictionary
students = {}

while True:
    print("\n===== Student Marks System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # adding a new student and marks
    if choice == "1":
        name = input("Enter student name: ")

        marks = float(input("Enter marks: "))

        students[name] = marks

        print("Student added successfully!")

    # displaying all students
    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(f"{name} : {marks}")

    # searching for a particular student
    elif choice == "3":

        search_name = input("Enter student name to search: ")

        if search_name in students:
            print(f"Marks of {search_name} = {students[search_name]}")
        else:
            print("Student not found.")

    # calculating average marks of all students
    elif choice == "4":

        if len(students) == 0:
            print("No records available.")

        else:
            total = sum(students.values())
            average = total / len(students)

            print(f"Average Marks = {average:.2f}")

    # exiting the program
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")