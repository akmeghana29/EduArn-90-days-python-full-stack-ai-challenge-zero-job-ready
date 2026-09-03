from flask import Flask
from config import Config
from extensions import db, login_manager
from routes.auth import auth_bp
from routes.jobs import jobs_bp
from routes.resumes import resumes_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth.login"

app.register_blueprint(auth_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(resumes_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
