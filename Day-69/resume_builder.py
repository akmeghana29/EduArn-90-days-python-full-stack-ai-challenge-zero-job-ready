import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_input(label, required=True):
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print("  This field is required. Please enter a value.")

def collect_details():
    print("\n--- Personal Details ---")
    name    = get_input("Full name")
    email   = get_input("Email")
    phone   = get_input("Phone")
    linkedin = get_input("LinkedIn URL (press Enter to skip)", required=False)
    github   = get_input("GitHub URL (press Enter to skip)", required=False)

    print("\n--- Education ---")
    education = get_input("Education (degree, college, year)")

    print("\n--- Experience ---")
    experience = get_input("Work experience (company, role, duration, what you did)")

    print("\n--- Skills ---")
    skills = get_input("Skills (comma separated)")

    print("\n--- Projects ---")
    projects = get_input("Projects (name and one line description each)")

    print("\n--- Job Target ---")
    job_role = get_input("What role are you applying for")

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "education": education,
        "experience": experience,
        "skills": skills,
        "projects": projects,
        "job_role": job_role
    }

def generate_resume(details):
    prompt = f"""
Build a professional resume for the following person applying for {details['job_role']}.

Name      : {details['name']}
Email     : {details['email']}
Phone     : {details['phone']}
LinkedIn  : {details['linkedin'] or 'Not provided'}
GitHub    : {details['github'] or 'Not provided'}
Education : {details['education']}
Experience: {details['experience']}
Skills    : {details['skills']}
Projects  : {details['projects']}

Write a clean, ATS friendly resume in plain text format.
Include sections: Contact, Summary, Education, Experience, Skills, Projects.
Write a strong professional summary tailored to the role.
Use action verbs and quantify achievements where possible.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume writer. Write ATS friendly, professional resumes that highlight the candidate's strengths clearly."
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
    print("        AI Resume Builder")
    print("=" * 40)
    print("\nAnswer the questions below to generate your resume.")

    details = collect_details()

    print("\nGenerating your resume...\n")
    resume = generate_resume(details)

    print("--- Your Resume ---\n")
    print(resume)
    print()

    save = input("Save resume to file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = f"{details['name'].replace(' ', '_')}_resume.txt"
        with open(filename, "w") as f:
            f.write(resume)
        print(f"Resume saved to {filename}")

if __name__ == "__main__":
    main()
