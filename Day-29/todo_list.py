"""
To-Do List
- Add a task
- View all tasks
- Mark task as done
- Delete a task
- Saved to todos.json
"""

import json
import sys
from pathlib import Path

FILE = "todos.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def view():
    tasks = load()
    if not tasks:
        print("\n  No tasks yet.\n")
        return
    print(f"\n  {'No':<4} {'Status':<10} Task")
    print("  " + "-" * 40)
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"  {i:<4} {status:<10} {t['task']}")
    print()

def add():
    task = input("Enter task: ").strip()
    if not task:
        print("\n  Task cannot be empty.\n")
        return
    tasks = load()
    tasks.append({"task": task, "done": False})
    save(tasks)
    print(f"\n  Task added.\n")

def mark_done():
    tasks = load()
    if not tasks:
        print("\n  No tasks found.\n")
        return
    view()
    choice = input("Enter task number to mark as done (0 to cancel): ").strip()
    if choice == "0":
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("\n  Invalid number.\n")
        return
    t = tasks[int(choice) - 1]
    if t["done"]:
        print("\n  Task is already marked as done.\n")
        return
    t["done"] = True
    save(tasks)
    print(f"\n  '{t['task']}' marked as done.\n")

def delete():
    tasks = load()
    if not tasks:
        print("\n  No tasks to delete.\n")
        return
    view()
    choice = input("Enter task number to delete (0 to cancel): ").strip()
    if choice == "0":
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("\n  Invalid number.\n")
        return
    removed = tasks.pop(int(choice) - 1)
    save(tasks)
    print(f"\n  '{removed['task']}' deleted.\n")

def main():
    print("=" * 35)
    print("          To-Do List")
    print("=" * 35)
    print()
    while True:
        print("[1] Add  [2] View  [3] Mark done  [4] Delete  [5] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("\n  Enter 1 to 5.\n")

if __name__ == "__main__":
    main()
