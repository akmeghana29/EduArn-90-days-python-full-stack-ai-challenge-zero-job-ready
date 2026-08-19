import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMAIL_TYPES = [
    "Job Application",
    "Follow Up",
    "Thank You",
    "Apology",
    "Meeting Request",
    "Project Update",
    "Resignation",
    "Cold Outreach"
]

TONES = ["Formal", "Friendly", "Assertive"]

def generate_email(email_type, tone, sender, recipient, details):
    prompt = f"""
Write a {tone.lower()} {email_type} email.
Sender   : {sender}
Recipient: {recipient}
Details  : {details}

Write only the email. Include Subject, greeting, body and sign off.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a professional email writer. Write clear, concise and well structured emails."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def pick_from_list(label, options):
    print(f"\n{label}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("  Invalid. Try again.")

def main():
    print("=" * 40)
    print("       AI Email Generator")
    print("=" * 40)
    print()

    email_type = pick_from_list("Select email type:", EMAIL_TYPES)
    tone       = pick_from_list("Select tone:", TONES)

    print()
    sender    = input("Your name       : ").strip()
    recipient = input("Recipient name  : ").strip()
    details   = input("Key details / context: ").strip()

    print("\nGenerating your email...\n")
    email = generate_email(email_type, tone, sender, recipient, details)

    print("--- Generated Email ---")
    print(email)
    print()

    save = input("Save to file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("generated_email.txt", "w") as f:
            f.write(email)
        print("Email saved to generated_email.txt")

if __name__ == "__main__":
    main()
