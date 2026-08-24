import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

REVIEW_TYPES = [
    "General Review",
    "Bug Detection",
    "Performance Improvements",
    "Security Issues",
    "Code Readability",
    "All of the above"
]

def review_code(code, language, review_type):
    prompt = f"""
Review the following {language} code for {review_type}.

Code:
{code}

Provide:
1. Summary of what the code does
2. Issues found
3. Suggestions to improve
4. Corrected version of the code if needed
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert software engineer and code reviewer. Review code clearly, find issues and suggest improvements with examples."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def get_code_from_input():
    print("\nPaste your code below. When done type END on a new line.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def get_code_from_file():
    path = input("Enter file path (eg. app.py): ").strip()
    if not os.path.exists(path):
        print("\n  File not found.\n")
        return None
    with open(path, "r") as f:
        return f.read()

def main():
    print("=" * 40)
    print("        AI Code Reviewer")
    print("=" * 40)
    print()

    # get code
    print("How do you want to provide the code?")
    print("  1. Paste code manually")
    print("  2. Load from file")
    while True:
        choice = input("\nChoice: ").strip()
        if choice == "1":
            code = get_code_from_input()
            break
        elif choice == "2":
            code = get_code_from_file()
            if code:
                break
        else:
            print("  Enter 1 or 2.")

    if not code.strip():
        print("\n  No code provided. Exiting.\n")
        return

    # language
    language = input("\nProgramming language (eg. Python, JavaScript): ").strip()
    if not language:
        language = "Python"

    # review type
    print("\nWhat kind of review do you want?")
    for i, r in enumerate(REVIEW_TYPES, 1):
        print(f"  {i}. {r}")
    while True:
        choice = input("\nChoice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(REVIEW_TYPES):
            review_type = REVIEW_TYPES[int(choice) - 1]
            break
        print("  Invalid choice.")

    print(f"\nReviewing your {language} code for {review_type}...\n")
    result = review_code(code, language, review_type)

    print("--- Review ---\n")
    print(result)
    print()

    save = input("Save review to file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("code_review.txt", "w") as f:
            f.write(f"Language    : {language}\n")
            f.write(f"Review Type : {review_type}\n")
            f.write(f"\n--- Original Code ---\n{code}\n")
            f.write(f"\n--- Review ---\n{result}\n")
        print("Review saved to code_review.txt")

if __name__ == "__main__":
    main()
