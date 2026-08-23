from flask import Blueprint, request, jsonify
from extensions import db
from models import CoverLetter
import openai
import os

cover_letter_bp = Blueprint("cover_letter", __name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(name, job_role, company, skills, experience):
    prompt = f"""
Write a professional cover letter for the following person.

Name       : {name}
Job Role   : {job_role}
Company    : {company}
Skills     : {skills}
Experience : {experience}

Write a concise, compelling and professional cover letter.
Include an opening, why they are a good fit, key skills and experience, and a closing.
Do not include a date or address header, just start from Dear Hiring Manager.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert cover letter writer. Write professional, tailored and compelling cover letters."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


# ---------- Generate and Save ----------

@cover_letter_bp.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name       = data.get("name", "").strip()
    email      = data.get("email", "").strip()
    job_role   = data.get("job_role", "").strip()
    company    = data.get("company", "").strip()
    skills     = data.get("skills", "").strip()
    experience = data.get("experience", "").strip()

    if not all([name, email, job_role, company, skills, experience]):
        return jsonify({"error": "All fields are required"}), 400

    cover_letter_text = generate_cover_letter(name, job_role, company, skills, experience)

    entry = CoverLetter(
        name=name,
        email=email,
        job_role=job_role,
        company=company,
        skills=skills,
        experience=experience,
        cover_letter=cover_letter_text
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({
        "message": "Cover letter generated",
        "cover_letter": entry.to_dict()
    }), 201


# ---------- Get All ----------

@cover_letter_bp.route("/cover-letters", methods=["GET"])
def get_all():
    letters = CoverLetter.query.order_by(CoverLetter.created_at.desc()).all()
    return jsonify({
        "total": len(letters),
        "cover_letters": [l.to_dict() for l in letters]
    }), 200


# ---------- Get One ----------

@cover_letter_bp.route("/cover-letters/<int:id>", methods=["GET"])
def get_one(id):
    letter = CoverLetter.query.get(id)
    if not letter:
        return jsonify({"error": "Not found"}), 404
    return jsonify(letter.to_dict()), 200


# ---------- Delete ----------

@cover_letter_bp.route("/cover-letters/<int:id>", methods=["DELETE"])
def delete(id):
    letter = CoverLetter.query.get(id)
    if not letter:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(letter)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200
