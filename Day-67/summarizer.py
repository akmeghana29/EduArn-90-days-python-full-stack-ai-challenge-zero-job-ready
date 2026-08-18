import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_resume(file_path):
    if not os.path.exists(file_path):
        print("File not found.")
        return None
    with open(file_path, "r") as f:
        return f.read()

def summarize_resume(resume_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert HR assistant. Summarize the given resume clearly and concisely. Include name, skills, experience, education and a one line overall summary."
            },
            {
                "role": "user",
                "content": f"Summarize this resume:\n\n{resume_text}"
            }
        ]
    )
    return response.choices[0].message.content

def main():
    print("=" * 40)
    print("       Resume Summarizer")
    print("=" * 40)
    print()

    file_path = input("Enter path to your resume (.txt file): ").strip()
    resume_text = read_resume(file_path)

    if not resume_text:
        return

    print("\nSummarizing your resume...\n")
    summary = summarize_resume(resume_text)
    print("--- Summary ---")
    print(summary)
    print()

    save = input("Save summary to a file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("resume_summary.txt", "w") as f:
            f.write(summary)
        print("Summary saved to resume_summary.txt")

if __name__ == "__main__":
    main()
