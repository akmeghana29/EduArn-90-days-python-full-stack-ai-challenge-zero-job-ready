# Expense Tracker

import json
import sys
from pathlib import Path
from datetime import date

EXPENSES_FILE="expenses.json"

CATEGORIES = [
    "Food", "Transport","Shopping",
    "Health", "Entertainment", "Bills", "Other"
]

# Storage

def load_expenses()-> list:
    if Path(EXPENSES_FILE).exists():
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses: list) -> None:
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


# Features
def add_expense():
    print("\n--- Add Expense ---")
    # Amount
    while True:
        amount = input("Amount spent (e.g. 250): ").strip()
        try:
            amount = float(amount )
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid positive number.\n")

    # Category
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Choose category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("Enter a number from the list.\n")

    # Description
    description = input("Description (optional): ").strip()
    if not description:
        description = "—"

    # Build entry
    entry = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses = load_expenses()
    expenses.append(entry)
    save_expenses(expenses)
    print(f"\nExpense of ₹{amount:.2f} added under '{category}'.\n")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\n  (No expenses recorded yet)\n")
        return

    print("\n--- All Expenses ---")
    print(f"  {'#':<4} {'Date':<12} {'Category':<15} {'Amount':>8}  Description")
    print("  " + "-" * 58)
    for i, e in enumerate(expenses, 1):
        print(f"  {i:<4} {e['date']:<12} {e['category']:<15} ₹{e['amount']:>7.2f}  {e['description']}")

    total = sum(e["amount"] for e in expenses)
    print("  " + "-" * 58)
    print(f"  {'TOTAL':<32} ₹{total:>7.2f}\n")


def view_by_category():
    expenses = load_expenses()
    if not expenses:
        print("\n  (No expenses recorded yet)\n")
        return

    # Group totals by category
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    grand_total = sum(totals.values())

    print("\n--- Spending by Category ---")
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    for cat, total in sorted_totals:
        percent = (total / grand_total) * 100
        bar = "" * int(percent // 5)
        print(f"  {cat:<15} ₹{total:>8.2f}  {percent:5.1f}%  {bar}")

    print(f"\n  Grand Total: ₹{grand_total:.2f}\n")


def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("\n  (No expenses to delete)\n")
        return

    view_expenses()
    while True:
        choice = input("Enter expense number to delete (or 0 to cancel): ").strip()
        if choice == "0":
            print()
            return
        if choice.isdigit() and 1 <= int(choice) <= len(expenses):
            removed = expenses.pop(int(choice) - 1)
            save_expenses(expenses)
            print(f"\nDeleted: ₹{removed['amount']:.2f} - {removed['category']} - {removed['description']}\n")
            return
        print("Invalid number.\n")


# Main 

def main():
    print("=" * 40)
    print("        Expense Tracker")
    print("=" * 40)
    print()

    while True:
        print("[1] Add expense")
        print("[2] View all expenses")
        print("[3] View by category")
        print("[4] Delete an expense")
        print("[5] Exit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Enter 1–5.\n")


if __name__ == "__main__":
    main()
