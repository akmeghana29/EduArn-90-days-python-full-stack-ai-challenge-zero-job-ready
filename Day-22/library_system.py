"""
Library System (OOP)
"""

import json
import sys
from pathlib import Path

FILE = "library.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---------- Book Class ----------

class Book:

    def __init__(self, title, author, status="Available", borrowed_by=None):
        self.title = title
        self.author = author
        self.status = status
        self.borrowed_by = borrowed_by

    def borrow(self, name):
        if self.status == "Borrowed":
            print(f"\n  Already borrowed by {self.borrowed_by}.\n")
            return
        self.status = "Borrowed"
        self.borrowed_by = name
        print(f"\n  '{self.title}' borrowed by {name}.\n")

    def return_book(self):
        if self.status == "Available":
            print(f"\n  '{self.title}' is already available.\n")
            return
        self.status = "Available"
        self.borrowed_by = None
        print(f"\n  '{self.title}' returned successfully.\n")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "status": self.status,
            "borrowed_by": self.borrowed_by
        }

# ---------- Library Class ----------

class Library:

    def __init__(self):
        self.books = [Book(b["title"], b["author"], b["status"], b["borrowed_by"]) for b in load()]

    def save_all(self):
        save([b.to_dict() for b in self.books])

    def add(self):
        title = input("Title: ").strip()
        if not title:
            print("\n  Title cannot be empty.\n")
            return
        if any(b.title.lower() == title.lower() for b in self.books):
            print(f"\n  '{title}' already exists.\n")
            return
        author = input("Author: ").strip() or "Unknown"
        self.books.append(Book(title, author))
        self.save_all()
        print(f"\n  '{title}' added to the library.\n")

    def view(self):
        if not self.books:
            print("\n  No books in the library.\n")
            return
        print(f"\n  {'No':<4} {'Title':<22} {'Author':<18} {'Status':<12} Borrowed By")
        print("  " + "-" * 65)
        for i, b in enumerate(self.books, 1):
            who = b.borrowed_by or "---"
            print(f"  {i:<4} {b.title:<22} {b.author:<18} {b.status:<12} {who}")
        print()

    def pick(self, action):
        self.view()
        if not self.books:
            return None
        choice = input(f"Enter book number to {action} (0 to cancel): ").strip()
        if choice == "0":
            return None
        if not choice.isdigit() or not (1 <= int(choice) <= len(self.books)):
            print("\n  Invalid number.\n")
            return None
        return int(choice) - 1

    def borrow(self):
        index = self.pick("borrow")
        if index is None:
            return
        name = input("Your name: ").strip()
        if not name:
            print("\n  Name cannot be empty.\n")
            return
        self.books[index].borrow(name)
        self.save_all()

    def return_book(self):
        borrowed = [b for b in self.books if b.status == "Borrowed"]
        if not borrowed:
            print("\n  No books currently borrowed.\n")
            return
        print(f"\n  {'No':<4} {'Title':<22} Borrowed By")
        print("  " + "-" * 40)
        for i, b in enumerate(borrowed, 1):
            print(f"  {i:<4} {b.title:<22} {b.borrowed_by}")
        print()
        choice = input("Enter book number to return (0 to cancel): ").strip()
        if choice == "0":
            return
        if not choice.isdigit() or not (1 <= int(choice) <= len(borrowed)):
            print("\n  Invalid number.\n")
            return
        borrowed[int(choice) - 1].return_book()
        self.save_all()

    def delete(self):
        index = self.pick("delete")
        if index is None:
            return
        b = self.books[index]
        if b.status == "Borrowed":
            print(f"\n  Cannot delete. Currently borrowed by {b.borrowed_by}.\n")
            return
        self.books.pop(index)
        self.save_all()
        print(f"\n  '{b.title}' deleted.\n")

# ---------- Main ----------

def main():
    print("=" * 35)
    print("       Library System")
    print("=" * 35)
    print()

    library = Library()

    while True:
        print("[1] Add  [2] View  [3] Borrow  [4] Return  [5] Delete  [6] Exit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            library.add()
        elif choice == "2":
            library.view()
        elif choice == "3":
            library.borrow()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.delete()
        elif choice == "6":
            print("\nThank you.")
            sys.exit(0)
        else:
            print("\n  Enter 1 to 6.\n")

if __name__ == "__main__":
    main()
