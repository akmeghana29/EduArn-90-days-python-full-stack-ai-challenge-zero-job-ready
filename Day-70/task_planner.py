import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_plan(goal, deadline, hours_per_day, skill_level):
    prompt = f"""
Create a detailed day by day task plan for the following goal.

Goal          : {goal}
Deadline      : {deadline}
Hours per day : {hours_per_day}
Skill level   : {skill_level}

Break the goal into daily tasks.
Each day should have a clear title and 2 to 4 specific tasks.
Keep tasks realistic and achievable within the given hours per day.
End with a short tip for staying on track.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a productivity expert and task planner. Create clear, realistic and actionable day by day plans to help people achieve their goals."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def main():
    print("=" * 40)
    print("         AI Task Planner")
    print("=" * 40)
    print()

    goal          = input("What is your goal: ").strip()
    deadline      = input("Deadline (eg. 7 days, 2 weeks, 1 month): ").strip()
    hours_per_day = input("How many hours can you spend per day: ").strip()

    print("\nSkill level:")
    print("  1. Beginner")
    print("  2. Intermediate")
    print("  3. Advanced")
    while True:
        choice = input("Choose: ").strip()
        if choice == "1":
            skill_level = "Beginner"
            break
        elif choice == "2":
            skill_level = "Intermediate"
            break
        elif choice == "3":
            skill_level = "Advanced"
            break
        else:
            print("  Enter 1, 2 or 3.")

    print("\nGenerating your plan...\n")
    plan = generate_plan(goal, deadline, hours_per_day, skill_level)

    print("--- Your Task Plan ---\n")
    print(plan)
    print()

    save = input("Save plan to file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = "task_plan.txt"
        with open(filename, "w") as f:
            f.write(f"Goal: {goal}\n")
            f.write(f"Deadline: {deadline}\n")
            f.write(f"Hours per day: {hours_per_day}\n")
            f.write(f"Skill level: {skill_level}\n\n")
            f.write(plan)
        print(f"Plan saved to {filename}")

if __name__ == "__main__":
    main()
