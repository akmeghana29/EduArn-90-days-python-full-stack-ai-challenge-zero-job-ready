from extensions import db
from datetime import datetime

class CoverLetter(db.Model):
    __tablename__ = "cover_letters"

    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100), nullable=False)
    email        = db.Column(db.String(100), nullable=False)
    job_role     = db.Column(db.String(100), nullable=False)
    company      = db.Column(db.String(100), nullable=False)
    skills       = db.Column(db.Text, nullable=False)
    experience   = db.Column(db.Text, nullable=False)
    cover_letter = db.Column(db.Text, nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id":           self.id,
            "name":         self.name,
            "email":        self.email,
            "job_role":     self.job_role,
            "company":      self.company,
            "skills":       self.skills,
            "experience":   self.experience,
            "cover_letter": self.cover_letter,
            "created_at":   self.created_at.strftime("%Y-%m-%d %H:%M")
        }
