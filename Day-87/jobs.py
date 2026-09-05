from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from extensions import db
from models import Job, Resume

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/dashboard")
@login_required
def dashboard():
    jobs = Job.query.filter_by(user_id=current_user.id).order_by(Job.created_at.desc()).all()
    job_data = []
    for job in jobs:
        total      = Resume.query.filter_by(job_id=job.id).count()
        shortlisted = Resume.query.filter_by(job_id=job.id, status="Shortlisted").count()
        rejected   = Resume.query.filter_by(job_id=job.id, status="Rejected").count()
        pending    = Resume.query.filter_by(job_id=job.id, status="Pending").count()
        job_data.append({
            "job":        job,
            "total":      total,
            "shortlisted": shortlisted,
            "rejected":   rejected,
            "pending":    pending
        })
    return render_template("dashboard.html", job_data=job_data)

@jobs_bp.route("/post-job", methods=["GET", "POST"])
@login_required
def post_job():
    if request.method == "POST":
        title           = request.form.get("title", "").strip()
        company         = request.form.get("company", "").strip()
        description     = request.form.get("description", "").strip()
        required_skills = request.form.get("required_skills", "").strip()

        if not title or not company or not description or not required_skills:
            flash("All fields are required.")
            return redirect(url_for("jobs.post_job"))

        job = Job(
            user_id=current_user.id,
            title=title,
            company=company,
            description=description,
            required_skills=required_skills
        )
        db.session.add(job)
        db.session.commit()
        flash("Job posted successfully.")
        return redirect(url_for("jobs.dashboard"))

    return render_template("post_job.html")

@jobs_bp.route("/job/<int:job_id>")
@login_required
def job_detail(job_id):
    job = Job.query.filter_by(id=job_id, user_id=current_user.id).first_or_404()
    resumes = Resume.query.filter_by(job_id=job.id).order_by(Resume.ai_score.desc()).all()
    return render_template("job_detail.html", job=job, resumes=resumes)

@jobs_bp.route("/job/<int:job_id>/delete", methods=["POST"])
@login_required
def delete_job(job_id):
    job = Job.query.filter_by(id=job_id, user_id=current_user.id).first_or_404()
    Resume.query.filter_by(job_id=job.id).delete()
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted.")
    return redirect(url_for("jobs.dashboard"))
