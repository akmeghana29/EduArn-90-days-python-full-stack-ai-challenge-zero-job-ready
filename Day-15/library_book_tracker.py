"""
Library Book Tracker
"""

import json
import sys
from pathlib import Path

FILE = "books.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(books):
    with open(FILE, "w") as f:
        json.dump(books, f, indent=2)

def show(books):
    if not books:
        print("\n  No books found.\n")
        return
    print(f"\n  {'#':<4} {'Title':<22} {'Author':<18} {'Status':<12} Borrowed By")
    print("  " + "-" * 65)
    for i, b in enumerate(books, 1):
        who = b["borrowed_by"] or "---"
        print(f"  {i:<4} {b['title']:<22} {b['author']:<18} {b['status']:<12} {who}")
    print()

def add():
    title = input("Title: ").strip()
    if not title:
        print("\n  Title cannot be empty.\n")
        return
    books = load()
    if any(b["title"].lower() == title.lower() for b in books):
        print(f"\n  '{title}' already exists.\n")
        return
    author = input("Author: ").strip() or "Unknown"
    books.append({"title": title, "author": author, "status": "Available", "borrowed_by": None})
    save(books)
    print(f"\n  '{title}' added.\n")

def borrow():
    books = load()
    show(books)
    choice = input("Book number to borrow (0 to cancel): ").strip()
    if choice == "0": return
    if not choice.isdigit() or not (1 <= int(choice) <= len(books)):
        print("\n  Invalid number.\n")
        return
    b = books[int(choice) - 1]
    if b["status"] == "Borrowed":
        print(f"\n  Already borrowed by {b['borrowed_by']}.\n")
        return
    name = input("Your name: ").strip()
    if not name:
        print("\n  Name cannot be empty.\n")
        return
    b["status"] = "Borrowed"
    b["borrowed_by"] = name
    save(books)
    print(f"\n  '{b['title']}' borrowed by {name}.\n")

def return_book():
    books = load()
    borrowed = [b for b in books if b["status"] == "Borrowed"]
    if not borrowed:
        print("\n  No books currently borrowed.\n")
        return
    show(borrowed)
    choice = input("Book number to return (0 to cancel): ").strip()
    if choice == "0": return
    if not choice.isdigit() or not (1 <= int(choice) <= len(borrowed)):
        print("\n  Invalid number.\n")
        return
    b = borrowed[int(choice) - 1]
    index = books.index(b)
    books[index]["status"] = "Available"
    books[index]["borrowed_by"] = None
    save(books)
    print(f"\n  '{b['title']}' returned.\n")

def delete():
    books = load()
    show(books)
    choice = input("Book number to delete (0 to cancel): ").strip()
    if choice == "0": return
    if not choice.isdigit() or not (1 <= int(choice) <= len(books)):
        print("\n  Invalid number.\n")
        return
    b = books[int(choice) - 1]
    if b["status"] == "Borrowed":
        print(f"\n  Cannot delete — currently borrowed by {b['borrowed_by']}.\n")
        return
    books.pop(int(choice) - 1)
    save(books)
    print(f"\n  '{b['title']}' deleted.\n")

def main():
    print("=" * 35)
    print("     Library Book Tracker")
    print("=" * 35 + "\n")
    while True:
        print("[1] Add  [2] View  [3] Borrow  [4] Return  [5] Delete  [6] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "1": add()
        elif choice == "2": show(load())
        elif choice == "3": borrow()
        elif choice == "4": return_book()
        elif choice == "5": delete()
        elif choice == "6": print("\nGoodbye."); sys.exit(0)
        else: print("\n  Enter 1 to 6.\n")

if __name__ == "__main__":
    main()
