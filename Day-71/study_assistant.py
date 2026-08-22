import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODES = [
    "Explain a topic",
    "Quiz me on a topic",
    "Summarize my notes",
    "Create a study plan",
    "Ask a doubt"
]

def ask(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

def explain_topic():
    topic = input("Enter topic to explain: ").strip()
    level = input("Your level (beginner / intermediate / advanced): ").strip()
    result = ask(
        "You are a patient and clear teacher. Explain topics simply with examples.",
        f"Explain {topic} for a {level} level student. Use simple language and give examples."
    )
    print(f"\n--- Explanation ---\n{result}\n")
    return result

def quiz_topic():
    topic = input("Enter topic to be quizzed on: ").strip()
    num   = input("How many questions (1-10): ").strip()
    result = ask(
        "You are a teacher creating quiz questions. Number each question clearly.",
        f"Create {num} multiple choice questions on {topic}. Give 4 options each and mark the correct answer at the end."
    )
    print(f"\n--- Quiz ---\n{result}\n")
    return result

def summarize_notes():
    print("Paste your notes below. When done type END on a new line.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    notes = "\n".join(lines)
    result = ask(
        "You are an expert note summarizer. Create concise and clear summaries.",
        f"Summarize these notes in simple bullet points:\n\n{notes}"
    )
    print(f"\n--- Summary ---\n{result}\n")
    return result

def create_study_plan():
    subject  = input("Subject or topic: ").strip()
    deadline = input("Deadline (eg. 3 days, 1 week): ").strip()
    hours    = input("Hours available per day: ").strip()
    result = ask(
        "You are a study planner. Create realistic and structured study plans.",
        f"Create a day by day study plan for {subject}. Deadline: {deadline}. Hours per day: {hours}."
    )
    print(f"\n--- Study Plan ---\n{result}\n")
    return result

def ask_doubt():
    subject = input("Subject: ").strip()
    doubt   = input("Your doubt or question: ").strip()
    result = ask(
        "You are a knowledgeable tutor. Answer student doubts clearly and thoroughly.",
        f"Subject: {subject}\nQuestion: {doubt}"
    )
    print(f"\n--- Answer ---\n{result}\n")
    return result

def save_output(content):
    save = input("Save this to file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("study_output.txt", "a") as f:
            f.write(content)
            f.write("\n" + "=" * 40 + "\n")
        print("Saved to study_output.txt\n")

def main():
    print("=" * 40)
    print("       AI Study Assistant")
    print("=" * 40)
    print()

    while True:
        print("What do you want to do?")
        for i, mode in enumerate(MODES, 1):
            print(f"  {i}. {mode}")
        print("  6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            result = explain_topic()
            save_output(result)
        elif choice == "2":
            result = quiz_topic()
            save_output(result)
        elif choice == "3":
            result = summarize_notes()
            save_output(result)
        elif choice == "4":
            result = create_study_plan()
            save_output(result)
        elif choice == "5":
            result = ask_doubt()
            save_output(result)
        elif choice == "6":
            print("\nGoodbye. Happy studying.")
            break
        else:
            print("\n  Enter 1 to 6.\n")

if __name__ == "__main__":
    main()
