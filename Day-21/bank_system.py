"""
Bank System using OOP

"""

import json
import sys
from pathlib import Path

FILE = "bank.json"

# ---------- Load and Save ----------

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---------- Account Class ----------

class BankAccount:

    def __init__(self, name, pin, balance=0, transactions=None):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = transactions if transactions else []

    def deposit(self, amount):
        if amount <= 0:
            print("\n  Amount must be greater than 0.\n")
            return
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"\n  Deposit successful. New balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n  Amount must be greater than 0.\n")
            return
        if amount > self.balance:
            print("\n  Not enough balance.\n")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        print(f"\n  Withdrawal successful. New balance: {self.balance}\n")

    def check_balance(self):
        print(f"\n  Account holder : {self.name}")
        print(f"  Current balance: {self.balance}\n")

    def view_history(self):
        if not self.transactions:
            print("\n  No transactions yet.\n")
            return
        print(f"\n  Transaction History for {self.name}")
        print("  " + "-" * 30)
        for i, t in enumerate(self.transactions, 1):
            print(f"  {i}. {t}")
        print()

    def to_dict(self):
        return {
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }

# ---------- Helper ----------

def get_account(username):
    data = load()
    if username in data:
        d = data[username]
        return BankAccount(d["name"], d["pin"], d["balance"], d["transactions"])
    return None

def save_account(username, account):
    data = load()
    data[username] = account.to_dict()
    save(data)

# ---------- Features ----------

def create_account():
    print("\n--- Create Account ---")
    username = input("Choose a username: ").strip()
    if not username:
        print("\n  Username cannot be empty.\n")
        return
    data = load()
    if username in data:
        print("\n  Username already taken.\n")
        return
    pin = input("Choose a 4 digit PIN: ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("\n  PIN must be exactly 4 digits.\n")
        return
    name = input("Enter your full name: ").strip()
    if not name:
        print("\n  Name cannot be empty.\n")
        return
    account = BankAccount(name, pin)
    save_account(username, account)
    print(f"\n  Account created successfully. Welcome, {name}.\n")

def login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    pin = input("PIN: ").strip()

    account = get_account(username)
    if account is None or account.pin != pin:
        print("\n  Invalid username or PIN.\n")
        return

    print(f"\n  Login successful. Welcome back, {account.name}.\n")

    while True:
        print("[1] Check balance")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Transaction history")
        print("[5] Logout")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = input("Enter amount to deposit: ").strip()
            if amount.isdigit():
                account.deposit(int(amount))
                save_account(username, account)
            else:
                print("\n  Enter a valid number.\n")
        elif choice == "3":
            amount = input("Enter amount to withdraw: ").strip()
            if amount.isdigit():
                account.withdraw(int(amount))
                save_account(username, account)
            else:
                print("\n  Enter a valid number.\n")
        elif choice == "4":
            account.view_history()
        elif choice == "5":
            print(f"\n  Logged out. Goodbye, {account.name}.\n")
            break
        else:
            print("\n  Enter 1 to 5.\n")

# ---------- Main ----------

def main():
    print("=" * 35)
    print("         Bank System")
    print("=" * 35)
    print()

    while True:
        print("[1] Create account")
        print("[2] Login")
        print("[3] Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("\n  Enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
