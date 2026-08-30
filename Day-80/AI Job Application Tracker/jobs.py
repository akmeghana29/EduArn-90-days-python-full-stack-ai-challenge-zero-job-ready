from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from extensions import db
from models import JobApplication
import openai
import os

jobs_bp = Blueprint("jobs", __name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

STATUSES = ["Applied", "Interview", "Offer", "Rejected"]

def generate_cover_letter(name, role, company, skills, experience):
    prompt = f"""
Write a professional cover letter for {name} applying for {role} at {company}.
Skills: {skills}
Experience: {experience}
Keep it concise, confident and professional. Start from Dear Hiring Manager.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert cover letter writer. Write professional and tailored cover letters."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


@jobs_bp.route("/dashboard")
@login_required
def dashboard():
    status_filter = request.args.get("status", "All")
    if status_filter == "All":
        jobs = JobApplication.query.filter_by(user_id=current_user.id).order_by(JobApplication.applied_date.desc()).all()
    else:
        jobs = JobApplication.query.filter_by(user_id=current_user.id, status=status_filter).order_by(JobApplication.applied_date.desc()).all()

    counts = {
        "All":       JobApplication.query.filter_by(user_id=current_user.id).count(),
        "Applied":   JobApplication.query.filter_by(user_id=current_user.id, status="Applied").count(),
        "Interview": JobApplication.query.filter_by(user_id=current_user.id, status="Interview").count(),
        "Offer":     JobApplication.query.filter_by(user_id=current_user.id, status="Offer").count(),
        "Rejected":  JobApplication.query.filter_by(user_id=current_user.id, status="Rejected").count(),
    }
    return render_template("dashboard.html", jobs=jobs, counts=counts, status_filter=status_filter, statuses=STATUSES)


@jobs_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_job():
    if request.method == "POST":
        company  = request.form.get("company", "").strip()
        role     = request.form.get("role", "").strip()
        location = request.form.get("location", "").strip()
        status   = request.form.get("status", "Applied")
        notes    = request.form.get("notes", "").strip()

        if not company or not role:
            flash("Company and role are required.")
            return redirect(url_for("jobs.add_job"))

        job = JobApplication(
            user_id=current_user.id,
            company=company,
            role=role,
            location=location,
            status=status,
            notes=notes
        )
        db.session.add(job)
        db.session.commit()
        flash("Job application added.")
        return redirect(url_for("jobs.dashboard"))

    return render_template("add_job.html", statuses=STATUSES)


@jobs_bp.route("/job/<int:job_id>", methods=["GET", "POST"])
@login_required
def job_detail(job_id):
    job = JobApplication.query.filter_by(id=job_id, user_id=current_user.id).first_or_404()

    if request.method == "POST":
        action = request.form.get("action")

        if action == "update":
            job.company  = request.form.get("company", job.company).strip()
            job.role     = request.form.get("role", job.role).strip()
            job.location = request.form.get("location", job.location).strip()
            job.status   = request.form.get("status", job.status)
            job.notes    = request.form.get("notes", job.notes).strip()
            db.session.commit()
            flash("Application updated.")

        elif action == "generate_cover_letter":
            skills     = request.form.get("skills", "").strip()
            experience = request.form.get("experience", "").strip()
            if not skills or not experience:
                flash("Please provide skills and experience to generate a cover letter.")
            else:
                job.cover_letter = generate_cover_letter(current_user.name, job.role, job.company, skills, experience)
                db.session.commit()
                flash("Cover letter generated.")

        elif action == "delete":
            db.session.delete(job)
            db.session.commit()
            flash("Application deleted.")
            return redirect(url_for("jobs.dashboard"))

    return render_template("job_detail.html", job=job, statuses=STATUSES)
