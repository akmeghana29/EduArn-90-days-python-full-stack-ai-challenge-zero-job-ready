import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DB_TYPES = ["MySQL", "PostgreSQL", "SQLite", "SQL Server", "Oracle"]

def generate_query(description, db_type, schema):
    schema_part = f"\nDatabase Schema:\n{schema}" if schema else ""
    prompt = f"""
Generate a {db_type} SQL query for the following requirement.

Requirement: {description}
{schema_part}

Provide:
1. The SQL query
2. A short explanation of what the query does
3. Example output if possible
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert SQL developer. Write clean, efficient and correct SQL queries. Always explain what the query does."
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
    print("      AI SQL Query Generator")
    print("=" * 40)
    print()

    while True:
        db_type     = pick("Select database type:", DB_TYPES)
        description = input("\nDescribe what you want the query to do:\n> ").strip()

        print("\nDo you have a schema to provide? (helps get accurate queries)")
        print("  1. Yes")
        print("  2. No")
        has_schema = input("Choice: ").strip()

        schema = ""
        if has_schema == "1":
            print("Paste your schema below. Type END on a new line when done.")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            schema = "\n".join(lines)

        print("\nGenerating SQL query...\n")
        result = generate_query(description, db_type, schema)

        print("--- Generated Query ---\n")
        print(result)
        print()

        save = input("Save to file? (yes/no): ").strip().lower()
        if save == "yes":
            with open("queries.txt", "a") as f:
                f.write(f"DB      : {db_type}\n")
                f.write(f"Request : {description}\n")
                f.write(f"\n{result}\n")
                f.write("\n" + "=" * 40 + "\n")
            print("Saved to queries.txt\n")

        again = input("Generate another query? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nGoodbye.")
            break
        print()

if __name__ == "__main__":
    main()
