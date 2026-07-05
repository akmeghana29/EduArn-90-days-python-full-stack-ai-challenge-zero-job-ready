"""
Student Grade Manager
- Add student with marks
- View all students with grade and percentage
- Delete a student
"""

import json
import sys
from pathlib import Path

FILE = "grades.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("\n  Name cannot be empty.\n")
        return
    students = load()
    if any(s["name"].lower() == name.lower() for s in students):
        print(f"\n  '{name}' already exists.\n")
        return
    marks = []
    subjects = ["Math", "Science", "English", "History", "Computer"]
    for subject in subjects:
        while True:
            mark = input(f"  {subject} marks (out of 100): ").strip()
            if mark.isdigit() and 0 <= int(mark) <= 100:
                marks.append(int(mark))
                break
            print("  Enter a number between 0 and 100.")
    students.append({"name": name, "marks": marks})
    save(students)
    print(f"\n  '{name}' added successfully.\n")

def view_students():
    students = load()
    if not students:
        print("\n  No students found.\n")
        return
    subjects = ["Math", "Sci", "Eng", "His", "Comp"]
    print(f"\n  {'No':<4} {'Name':<18} {' '.join(f'{s:<5}' for s in subjects)} {'Avg':>6} {'Grade':>6}")
    print("  " + "-" * 60)
    for i, s in enumerate(students, 1):
        avg = sum(s["marks"]) / len(s["marks"])
        grade = get_grade(avg)
        marks_str = " ".join(f"{m:<5}" for m in s["marks"])
        print(f"  {i:<4} {s['name']:<18} {marks_str} {avg:>6.1f} {grade:>6}")
    print()

def delete_student():
    students = load()
    if not students:
        print("\n  No students to delete.\n")
        return
    view_students()
    choice = input("Enter student number to delete (0 to cancel): ").strip()
    if choice == "0":
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(students)):
        print("\n  Invalid number.\n")
        return
    removed = students.pop(int(choice) - 1)
    save(students)
    print(f"\n  '{removed['name']}' deleted.\n")

def main():
    print("=" * 35)
    print("     Student Grade Manager")
    print("=" * 35)
    print()
    while True:
        print("[1] Add student  [2] View all  [3] Delete  [4] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("\n  Enter 1 to 4.\n")

if __name__ == "__main__":
    main()
