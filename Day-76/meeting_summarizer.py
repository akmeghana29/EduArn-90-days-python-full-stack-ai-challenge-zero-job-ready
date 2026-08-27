import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(notes, meeting_title):
    prompt = f"""
Summarize the following meeting notes for the meeting titled: {meeting_title}

Meeting Notes:
{notes}

Provide:
1. Meeting Summary (2-3 sentences)
2. Key Discussion Points (bullet points)
3. Decisions Made
4. Action Items (who needs to do what)
5. Follow Up Required (yes/no and why)
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert meeting assistant. Summarize meeting notes clearly, extract action items and highlight key decisions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def get_notes_from_paste():
    print("\nPaste your meeting notes below. Type END on a new line when done.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def get_notes_from_file():
    path = input("Enter file path (eg. notes.txt): ").strip()
    if not os.path.exists(path):
        print("\n  File not found.\n")
        return None
    with open(path, "r") as f:
        return f.read()

def main():
    print("=" * 40)
    print("   AI Meeting Notes Summarizer")
    print("=" * 40)
    print()

    meeting_title = input("Meeting title: ").strip()
    if not meeting_title:
        meeting_title = "Untitled Meeting"

    print("\nHow do you want to provide the notes?")
    print("  1. Paste notes manually")
    print("  2. Load from a .txt file")

    while True:
        choice = input("\nChoice: ").strip()
        if choice == "1":
            notes = get_notes_from_paste()
            break
        elif choice == "2":
            notes = get_notes_from_file()
            if notes:
                break
        else:
            print("  Enter 1 or 2.")

    if not notes.strip():
        print("\n  No notes provided. Exiting.\n")
        return

    print("\nSummarizing meeting notes...\n")
    summary = summarize(notes, meeting_title)

    print("--- Meeting Summary ---\n")
    print(summary)
    print()

    save = input("Save summary to file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = f"{meeting_title.replace(' ', '_')}_summary.txt"
        with open(filename, "w") as f:
            f.write(f"Meeting : {meeting_title}\n")
            f.write("=" * 40 + "\n\n")
            f.write(summary)
        print(f"Summary saved to {filename}")

if __name__ == "__main__":
    main()
