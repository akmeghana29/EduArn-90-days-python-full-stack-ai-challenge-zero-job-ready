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
    jobs       = db.relationship("JobApplication", backref="user", lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class JobApplication(db.Model):
    __tablename__ = "job_applications"

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    company      = db.Column(db.String(100), nullable=False)
    role         = db.Column(db.String(100), nullable=False)
    location     = db.Column(db.String(100))
    status       = db.Column(db.String(50), default="Applied")
    notes        = db.Column(db.Text)
    cover_letter = db.Column(db.Text)
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id":           self.id,
            "company":      self.company,
            "role":         self.role,
            "location":     self.location,
            "status":       self.status,
            "notes":        self.notes,
            "cover_letter": self.cover_letter,
            "applied_date": self.applied_date.strftime("%d %b %Y")
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
