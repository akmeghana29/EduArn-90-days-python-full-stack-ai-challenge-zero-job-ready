from extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    jobs       = db.relationship("Job", backref="created_by", lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Job(db.Model):
    __tablename__ = "jobs"

    id              = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title           = db.Column(db.String(100), nullable=False)
    company         = db.Column(db.String(100), nullable=False)
    description     = db.Column(db.Text, nullable=False)
    required_skills = db.Column(db.Text, nullable=False)
    created_at      = db.Column(db.DateTime, default=datetime.utcnow)
    resumes         = db.relationship("Resume", backref="job", lazy=True)


class Resume(db.Model):
    __tablename__ = "resumes"

    id               = db.Column(db.Integer, primary_key=True)
    job_id           = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=False)
    applicant_name   = db.Column(db.String(100), nullable=False)
    applicant_email  = db.Column(db.String(120), nullable=False)
    filename         = db.Column(db.String(200), nullable=False)
    resume_text      = db.Column(db.Text)
    ai_score         = db.Column(db.Float, default=0.0)
    ai_summary       = db.Column(db.Text)
    matched_skills   = db.Column(db.Text)
    missing_skills   = db.Column(db.Text)
    status           = db.Column(db.String(50), default="Pending")
    uploaded_at      = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
