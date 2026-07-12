"""
User Profile System
- Register with username and password
- Login
- View your profile
- Edit your profile
- Delete your account
- Saved to profiles.json
"""

import json
import sys
from pathlib import Path

FILE = "profiles.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def register():
    print("\n--- Register ---")
    username = input("Choose a username: ").strip()
    if not username:
        print("\n  Username cannot be empty.\n")
        return
    data = load()
    if username in data:
        print("\n  Username already taken.\n")
        return
    password = input("Choose a password: ").strip()
    if not password:
        print("\n  Password cannot be empty.\n")
        return
    print("\n  Fill in your profile details (press Enter to skip):")
    name     = input("  Full name : ").strip() or "Not set"
    age      = input("  Age       : ").strip() or "Not set"
    email    = input("  Email     : ").strip() or "Not set"
    bio      = input("  Bio       : ").strip() or "Not set"
    interest = input("  Interests : ").strip() or "Not set"

    data[username] = {
        "password": password,
        "name": name,
        "age": age,
        "email": email,
        "bio": bio,
        "interests": interest
    }
    save(data)
    print(f"\n  Account created. Welcome, {name}.\n")

def login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    data = load()
    if username not in data or data[username]["password"] != password:
        print("\n  Invalid username or password.\n")
        return

    print(f"\n  Login successful. Welcome back, {data[username]['name']}.\n")
    account_menu(username)

def view_profile(username):
    data = load()
    p = data[username]
    print(f"\n  --- Profile of {username} ---")
    print(f"  Name      : {p['name']}")
    print(f"  Age       : {p['age']}")
    print(f"  Email     : {p['email']}")
    print(f"  Bio       : {p['bio']}")
    print(f"  Interests : {p['interests']}\n")

def edit_profile(username):
    data = load()
    p = data[username]
    print("\n  Press Enter to keep current value.\n")
    name     = input(f"  Full name  ({p['name']}): ").strip()
    age      = input(f"  Age        ({p['age']}): ").strip()
    email    = input(f"  Email      ({p['email']}): ").strip()
    bio      = input(f"  Bio        ({p['bio']}): ").strip()
    interest = input(f"  Interests  ({p['interests']}): ").strip()

    if name:     p["name"]      = name
    if age:      p["age"]       = age
    if email:    p["email"]     = email
    if bio:      p["bio"]       = bio
    if interest: p["interests"] = interest

    data[username] = p
    save(data)
    print("\n  Profile updated.\n")

def delete_account(username):
    confirm = input("  Are you sure you want to delete your account? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("\n  Cancelled.\n")
        return
    data = load()
    del data[username]
    save(data)
    print("\n  Account deleted.\n")
    main_menu()
    sys.exit(0)

def account_menu(username):
    while True:
        print("[1] View profile  [2] Edit profile  [3] Delete account  [4] Logout")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            edit_profile(username)
        elif choice == "3":
            delete_account(username)
            return
        elif choice == "4":
            print("\n  Logged out.\n")
            return
        else:
            print("\n  Enter 1 to 4.\n")

def main_menu():
    while True:
        print("[1] Register  [2] Login  [3] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("\n  Enter 1, 2, or 3.\n")

def main():
    print("=" * 35)
    print("      User Profile System")
    print("=" * 35)
    print()
    main_menu()

if __name__ == "__main__":
    main()
