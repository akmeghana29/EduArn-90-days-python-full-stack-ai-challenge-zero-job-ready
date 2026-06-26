"""
Contact Book
"""

import json
import sys
from pathlib import Path

CONTACTS_FILE = "contacts.json"
#Load and Save

def load_contacts():
    if Path(CONTACTS_FILE).exists():
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

# Show

def show_all():
    contacts = load_contacts()

    if not contacts:
        print("\n  (No contacts saved yet)\n")
        return

    print(f"\n--- All Contacts ({len(contacts)}) ---")
    print(f"  {'#':<4} {'Name':<20} {'Phone':<15} Email")
    print("  " + "-" * 55)
    for i, c in enumerate(contacts, 1):
        print(f"  {i:<4} {c['name']:<20} {c['phone']:<15} {c['email']}")
    print()

# Add
def add_contact():
    print("\n--- Add Contact ---")

    name = input("Name: ").strip()
    if not name:
        print(" Name cannot be empty.\n")
        return

    # check if name already exists
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f" A contact named '{name}' already exists.\n")
            return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contact = {
        "name": name,
        "phone": phone if phone else "—",
        "email": email if email else "—"
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"\n✓ Contact '{name}' added.\n")

# Search

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name to search: ").strip().lower()

    contacts = load_contacts()
    results = [c for c in contacts if query in c["name"].lower()]

    if not results:
        print(f"\n  No contacts found matching '{query}'.\n")
        return

    print(f"\n  Found {len(results)} result(s):")
    print(f"  {'Name':<20} {'Phone':<15} Email")
    print("  " + "-" * 50)
    for c in results:
        print(f"  {c['name']:<20} {c['phone']:<15} {c['email']}")
    print()

#Edit

def edit_contact():
    contacts = load_contacts()
    if not contacts:
        print("\n  (No contacts to edit)\n")
        return

    show_all()
    choice = input("Enter contact number to edit (or 0 to cancel): ").strip()

    if choice == "0":
        print()
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(contacts)):
        print(" Invalid number.\n")
        return

    index = int(choice) - 1
    contact = contacts[index]

    print(f"\nEditing '{contact['name']}' — press Enter to keep current value\n")

    new_name = input(f"Name ({contact['name']}): ").strip()
    new_phone = input(f"Phone ({contact['phone']}): ").strip()
    new_email = input(f"Email ({contact['email']}): ").strip()

    # only update if user typed something new
    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email

    contacts[index] = contact
    save_contacts(contacts)
    print(f"\n Contact updated.\n")

# Delete

def delete_contact():
    contacts = load_contacts()
    if not contacts:
        print("\n  (No contacts to delete)\n")
        return

    show_all()
    choice = input("Enter contact number to delete (or 0 to cancel): ").strip()

    if choice == "0":
        print()
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(contacts)):
        print(" Invalid number.\n")
        return

    index = int(choice) - 1
    removed = contacts.pop(index)
    save_contacts(contacts)
    print(f"\n '{removed['name']}' deleted.\n")

# Main

def main():
    print("=" * 40)
    print("         Contact Book")
    print("=" * 40)
    print()

    while True:
        print("[1] Add contact")
        print("[2] View all contacts")
        print("[3] Search contact")
        print("[4] Edit contact")
        print("[5] Delete contact")
        print("[6] Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Enter 1–6.\n")

if __name__ == "__main__":
    main()
