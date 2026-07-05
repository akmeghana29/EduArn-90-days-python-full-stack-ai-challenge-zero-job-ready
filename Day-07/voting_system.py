# VOTING SYSTEM

import sys

ADMIN_PASSWORD = "admin123"  

candidates = {} 
voters = set()    

def admin_login() -> bool:
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        print("Admin access granted.\n")
        return True
    print("Wrong password.\n")
    return False


def add_candidate():
    name = input("Enter candidate name to add: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return
    if name.lower() in [c.lower() for c in candidates]:
        print(f"'{name}' already exists.\n")
        return
    candidates[name] = 0
    print(f"Candidate '{name}' added.\n")


def remove_candidate():
    if not candidates:
        print("No candidates to remove.\n")
        return
    show_candidates()
    name = input("Enter candidate name to remove: ").strip()
    match = next((c for c in candidates if c.lower() == name.lower()), None)
    if match:
        del candidates[match]
        print(f"Candidate '{match}' removed.\n")
    else:
        print(f"Candidate '{name}' not found.\n")


def admin_menu():
    if not admin_login():
        return
    while True:
        print("--- Admin Menu ---")
        print("[1] Add candidate")
        print("[2] Remove candidate")
        print("[3] View results")
        print("[4] Back to main menu")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_candidate()
        elif choice == "2":
            remove_candidate()
        elif choice == "3":
            show_results()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")


def show_candidates():
    if not candidates:
        print("  (No candidates yet)\n")
        return
    print("\n  Candidates:")
    for i, name in enumerate(candidates, 1):
        print(f"  {i}. {name}")
    print()


def cast_vote():
    if not candidates:
        print("No candidates available to vote for yet.\n")
        return

    voter_name = input("Enter your name: ").strip()
    if not voter_name:
        print("Name cannot be empty.\n")
        return
    if voter_name.lower() in [v.lower() for v in voters]:
        print(f" '{voter_name}' has already voted.\n")
        return

    show_candidates()
    choice = input("Enter candidate name to vote for: ").strip()
    match = next((c for c in candidates if c.lower() == choice.lower()), None)

    if not match:
        print(f"Candidate '{choice}' not found.\n")
        return

    candidates[match] += 1
    voters.add(voter_name)
    print(f"Vote cast for '{match}'. Thank you, {voter_name}!\n")


def show_results():
    print("\n--- Current Results ---")
    if not candidates:
        print("  (No candidates yet)\n")
        return

    total = sum(candidates.values())
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

    for rank, (name, votes) in enumerate(sorted_candidates, 1):
        percent = (votes / total * 100) if total > 0 else 0
        bar = "" * int(percent // 5) 
        print(f"  {rank}. {name:<20} {votes} vote(s)  {percent:5.1f}%  {bar}")

    print(f"\n  Total votes cast: {total}")
    print(f"  Total voters    : {len(voters)}\n")

    if total > 0:
        leader = sorted_candidates[0][0]
        print(f" Currently leading: {leader}\n")


def main():
    print("=" * 40)
    print("        Voting System")
    print("=" * 40)
    print()

    while True:
        print("[1] Admin panel")
        print("[2] Cast a vote")
        print("[3] View results")
        print("[4] Exit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            print()
            admin_menu()
        elif choice == "2":
            print()
            cast_vote()
        elif choice == "3":
            show_results()
        elif choice == "4":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
