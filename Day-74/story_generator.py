import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GENRES = ["Fantasy", "Mystery", "Romance", "Horror", "Sci-Fi", "Adventure", "Comedy"]
LENGTHS = ["Short (300 words)", "Medium (600 words)", "Long (1000 words)"]

def generate_story(genre, theme, character, setting, length):
    prompt = f"""
Write a {genre} story with the following details.

Theme     : {theme}
Character : {character}
Setting   : {setting}
Length    : {length}

Write only the story with a title. Make it engaging and creative.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a creative story writer. Write engaging, imaginative and well structured stories."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def pick(label, options):
    print(f"\n{label}")
    for i, o in enumerate(options, 1):
        print(f"  {i}. {o}")
    while True:
        choice = input("Choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("  Invalid. Try again.")

def main():
    print("=" * 40)
    print("       AI Story Generator")
    print("=" * 40)
    print()

    genre     = pick("Select genre:", GENRES)
    length    = pick("Select length:", LENGTHS)

    print()
    theme     = input("Theme or plot idea   : ").strip()
    character = input("Main character name  : ").strip()
    setting   = input("Setting / location   : ").strip()

    print("\nGenerating your story...\n")
    story = generate_story(genre, theme, character, setting, length)

    print("--- Your Story ---\n")
    print(story)
    print()

    save = input("Save story to file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = f"{character.replace(' ', '_')}_story.txt"
        with open(filename, "w") as f:
            f.write(story)
        print(f"Story saved to {filename}")

if __name__ == "__main__":
    main()
