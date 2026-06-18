# LOGIN SYSTEM USING PYTHON

import json
import os
import sys
import getpass
from pathlib import Path

try:
    import bcrypt
    USE_BCRYPT = True
except ImportError:
    import hashlib
    import secrets
    USE_BCRYPT = False

USERS_FILE = "users.json"


# Storage 

def load_users() -> dict:
    if Path(USERS_FILE).exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users: dict) -> None:
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


# Hashing

def hash_password(password: str) -> str:
    if USE_BCRYPT:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    else:
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256((salt + password).encode()).hexdigest()
        return f"{salt}:{hashed}"


def verify_password(password: str, stored: str) -> bool:
    if USE_BCRYPT:
        return bcrypt.checkpw(password.encode(), stored.encode())
    else:
        salt, hashed = stored.split(":", 1)
        return hashlib.sha256((salt + password).encode()).hexdigest() == hashed


# Authentication

def register(username: str, password: str) -> tuple[bool, str]:
    if len(username.strip()) < 3:
        return False, "Username must be at least 3 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    users = load_users()
    if username in users:
        return False, f"Username '{username}' already exists."

    users[username] = {"password": hash_password(password)}
    save_users(users)
    return True, f"User '{username}' registered successfully."


def login(username: str, password: str) -> tuple[bool, str]:
    users = load_users()
    if username not in users:
        return False, "Invalid username or password."
    if not verify_password(password, users[username]["password"]):
        return False, "Invalid username or password."
    return True, f"Welcome back, {username}!"


def prompt_credentials(action: str) -> tuple[str, str]:
    print(f"\n--- {action} ---")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    return username, password


def main():
    print("=" * 40)
    print("       Simple Login System")
    if not USE_BCRYPT:
        print("  (bcrypt not found; using hashlib)")
    print("=" * 40)

    while True:
        print("\n[1] Register")
        print("[2] Login")
        print("[3] Exit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            username, password = prompt_credentials("Register")
            ok, msg = register(username, password)
            print(f"\n{'✓' if ok else '✗'} {msg}")

        elif choice == "2":
            username, password = prompt_credentials("Login")
            ok, msg = login(username, password)
            print(f"\n{'✓' if ok else '✗'} {msg}")
            if ok:
                print(f"  [Session active for: {username}]")

        elif choice == "3":
            print("\nThank You.")
            sys.exit(0)

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
